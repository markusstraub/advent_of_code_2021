#%%
import sys
import itertools
import more_itertools
from collections import namedtuple

NoteEntry = namedtuple("NoteEntry", "patterns output")


def gen_note_entries(filename="test_advent08.txt"):
    """return test data if no file is given"""
    with open(filename) as file:
        for line in file:
            tokens = line.strip().split(" | ")
            yield NoteEntry(tokens[0].split(" "), tokens[1].split(" "))


# %%
print(list(gen_note_entries()))


def count_1478(entries):
    count = 0
    for entry in entries:
        by_len = more_itertools.map_reduce(entry.output, keyfunc=len, reducefunc=len)
        only_1478 = {k: v for k, v in by_len.items() if k in [2, 3, 4, 7]}
        count += sum(only_1478.values())
    return count


count = count_1478(gen_note_entries("advent08.txt"))
print(f"part1: found {count} instances of 1, 4, 7 or 8 in the entries' outputs")

# %%
