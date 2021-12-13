from collections import defaultdict
from collections import Counter
import more_itertools

FILENAME = "advent12.txt"
TEST_FILENAME = "test_advent12.txt"


def as_new_list(iterable_or_string):
    if isinstance(iterable_or_string, str):
        new_list = list()
        new_list.append(iterable_or_string)
        return new_list
    return [v for v in iterable_or_string]


def is_small_cave(name):
    return name == name.lower()


def filter_small_caves_only_once(path, next_cave, start):
    if is_small_cave(next_cave) and next_cave in as_new_list(path):
        return False
    return True


def filter_small_caves_only_twice(path, next_cave, start):
    path = as_new_list(path)
    if next_cave == start:
        return False
    if not is_small_cave(next_cave):
        return True

    small_cave_occurrences = Counter(filter(is_small_cave, path))
    two_or_more_visits = more_itertools.ilen(
        filter(lambda x: x >= 2, small_cave_occurrences.values())
    )
    visit_limit = 2 if two_or_more_visits == 0 else 1

    if path.count(next_cave) >= visit_limit:
        return False
    return True


class Caves:
    def __init__(self, filename=TEST_FILENAME):
        self._edges = defaultdict(set)
        with open(filename) as file:
            for line in file:
                start, end = line.strip().split("-")
                self._edges[start].add(end)
                self._edges[end].add(start)

    def find_all_paths(self, start, end, exploration_filter):
        full_paths = list()
        partial_paths = as_new_list(start)

        while True:
            new_partial_paths = list()
            for partial_path in partial_paths:
                extended_paths = list()
                current_cave = as_new_list(partial_path)[-1]
                # print(f"{partial_path=} .. {current_cave=}")
                for to_cave in self._edges[current_cave]:
                    if not exploration_filter(partial_path, to_cave, start):
                        continue
                    # print(f"exploring path towards {to_cave}")
                    new_partial = as_new_list(partial_path)
                    new_partial.append(to_cave)
                    extended_paths.append(tuple(new_partial))

                # print(f"{extended_paths=}")
                for extended_path in extended_paths:
                    finished = extended_path[-1] == end
                    if finished:
                        full_paths.append(extended_path)
                    else:
                        new_partial_paths.append(extended_path)

            partial_paths = new_partial_paths
            if len(partial_paths) == 0:
                break

        return full_paths


START = "start"
END = "end"

# caves = Caves()
# paths = caves.find_all_paths(START, END, filter_small_caves_only_twice)
# print("\n".join(sorted([",".join(list(path)) for path in paths])))

if __name__ == "__main__":
    caves = Caves(FILENAME)
    paths = caves.find_all_paths(START, END, filter_small_caves_only_once)
    print(f"part1: {len(paths)} paths when small caves can only be visited once.")

    paths = caves.find_all_paths(START, END, filter_small_caves_only_twice)
    print(
        f"part2: {len(paths)} paths when small caves can only be visited once",
        "(except for one cave that can be visited twice).",
    )
