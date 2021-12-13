#%%
import itertools
from collections import namedtuple
from collections import defaultdict

FILENAME = "advent12.txt"
TEST_FILENAME = "test_advent12.txt"


def is_small_cave(name):
    return name == name.lower()


def as_new_list(iterable_or_string):
    if isinstance(iterable_or_string, str):
        new_list = list()
        new_list.append(iterable_or_string)
        return new_list
    return [v for v in iterable_or_string]


#%%


class Caves:
    def __init__(self, filename=TEST_FILENAME):
        self._edges = defaultdict(set)
        with open(filename) as file:
            for line in file:
                start, end = line.strip().split("-")
                self._edges[start].add(end)
                self._edges[end].add(start)

    def find_all_paths(self, start, end):
        full_paths = list()
        partial_paths = as_new_list(start)

        while True:
            new_partial_paths = list()
            for partial_path in partial_paths:
                extended_paths = list()
                current_cave = as_new_list(partial_path)[-1]
                print(f"{partial_path=} .. {current_cave=}")
                for to_cave in self._edges[current_cave]:
                    if is_small_cave(to_cave) and to_cave in as_new_list(partial_path):
                        continue
                    print(f"exploring path towards {to_cave}")
                    new_partial = as_new_list(partial_path)
                    new_partial.append(to_cave)
                    extended_paths.append(tuple(new_partial))

                print(f"{extended_paths=}")

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

caves = Caves()
print(caves._edges)
print(caves.find_all_paths(START, END))
# %%
