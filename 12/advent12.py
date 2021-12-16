from collections import defaultdict
from collections import Counter
import more_itertools

FILENAME = "advent12.txt"
TEST_FILENAME = "test_advent12.txt"


def is_small_cave(name):
    return name == name.lower()


def filter_small_caves_only_once(path, next_cave, start):
    return is_small_cave(next_cave) and next_cave in path


def filter_small_caves_only_twice(path, next_cave, start):
    if next_cave == start:
        return True
    if not is_small_cave(next_cave):
        return False

    small_cave_occurrences = Counter(filter(is_small_cave, path))
    two_or_more_visits = more_itertools.ilen(
        filter(lambda x: x >= 2, small_cave_occurrences.values())
    )
    visit_limit = 2 if two_or_more_visits == 0 else 1
    return path.count(next_cave) >= visit_limit


class Caves:
    def __init__(self, filename=TEST_FILENAME):
        self._edges = defaultdict(set)
        with open(filename) as file:
            for line in file:
                start, end = line.strip().split("-")
                self._edges[start].add(end)
                self._edges[end].add(start)

    def find_all_paths(self, start, end, exploration_filter):
        full_paths = []
        partial_paths = [[start]]

        while True:
            new_partial_paths = []
            for partial_path in partial_paths:
                extended_paths = []
                current_cave = partial_path[-1]
                # print(f"{partial_path=} .. {current_cave=}")
                for to_cave in self._edges[current_cave]:
                    if exploration_filter(partial_path, to_cave, start):
                        continue
                    # print(f"exploring path towards {to_cave}")
                    extended_paths.append(partial_path + [to_cave])

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


if __name__ == "__main__":
    caves = Caves(FILENAME)
    start_cave = "start"
    end_cave = "end"

    paths = caves.find_all_paths(start_cave, end_cave, filter_small_caves_only_once)
    print(f"part1: {len(paths)} paths when small caves can only be visited once.")

    paths = caves.find_all_paths(start_cave, end_cave, filter_small_caves_only_twice)
    print(
        f"part2: {len(paths)} paths when small caves can only be visited once",
        "(except for one cave that can be visited twice).",
    )
