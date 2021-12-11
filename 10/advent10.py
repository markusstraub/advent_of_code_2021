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


#%%


def check_validity(nav_chunk):
    stack = list()
    for bracket in nav_chunk:
        if bracket in OPENING:
            stack.append(bracket)
        else:
            open_bracket = stack.pop()
            if not OPEN2CLOSE[open_bracket] == bracket:
                return SCORES.get(bracket)
    return 0


total_error = sum([check_validity(chunk) for chunk in read_input("advent10.txt")])
print(f"part1: {total_error}")

#%%
total_error = 0
for chunk in read_input("advent10.txt"):
    error = check_validity(chunk)
    print(f"{chunk=} error index: {error})")
    total_error += error
print(total_error)

# %%
