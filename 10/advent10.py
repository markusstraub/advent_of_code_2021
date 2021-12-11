#%%
from collections import namedtuple


SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
OPENING = "({[<"
OPEN2CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}


def read_input(filename="test_advent10.txt"):
    """return test data if no file is given"""
    with open(filename) as file:
        for line in file:
            yield line.strip()


def check_validity(nav_chunk):
    stack = list()
    for bracket in nav_chunk:
        if bracket in OPENING:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return SCORES.get(bracket)
            open_bracket = stack.pop()
            if not OPEN2CLOSE[open_bracket] == bracket:
                return SCORES.get(bracket)
    return 0


#%%

if __name__ == "__main__":
    total_error = sum([check_validity(chunk) for chunk in read_input("advent10.txt")])
    print(f"part1: total score for corrupted lines: {total_error}")


# %%
