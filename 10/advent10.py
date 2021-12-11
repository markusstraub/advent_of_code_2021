from collections import namedtuple


CORRUPTION_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETION_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}
OPENING_BRACKETS = "({[<"
OPEN2CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}
TEST_FILENAME = "test_advent10.txt"


def read_input(filename=TEST_FILENAME):
    """return test data if no file is given"""
    with open(filename) as file:
        for line in file:
            yield line.strip()


def calc_corruption_score(nav_line):
    stack = list()
    for bracket in nav_line:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return CORRUPTION_SCORES.get(bracket)
            open_bracket = stack.pop()
            if not OPEN2CLOSE[open_bracket] == bracket:
                return CORRUPTION_SCORES.get(bracket)
    return 0


def calc_autocompletion_score(nav_line):
    """returns 0 for corrupt lines"""
    if calc_corruption_score(nav_line) > 0:
        return 0
    stack = list()
    for bracket in nav_line:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                raise Exception(f"invalid nav line {nav_line}")
            open_bracket = stack.pop()
            if not OPEN2CLOSE[open_bracket] == bracket:
                raise Exception(f"invalid nav line {nav_line}")

    # autocomplete open brackets
    score = 0
    autocomplete = ""
    for open_bracket in reversed(stack):
        closing_bracket = OPEN2CLOSE.get(open_bracket)
        autocomplete += closing_bracket
        score *= 5
        score += AUTOCOMPLETION_SCORES.get(closing_bracket)
    # print(f"autocompleted: {nav_line} + {autocomplete}")
    return score


def calc_middle_autocompletion_score(filename=TEST_FILENAME):
    scores = [calc_autocompletion_score(line) for line in read_input(filename)]
    scores = list(sorted(filter(None, scores)))
    return scores[int(len(scores) / 2)]


if __name__ == "__main__":
    input_file = "advent10.txt"
    total_error = sum(
        [calc_corruption_score(nav_line) for nav_line in read_input(input_file)]
    )
    print(f"part1: total score for corrupted navigation chunks: {total_error}")

    middle_autocompletion_score = calc_middle_autocompletion_score(input_file)
    print(f"part2: middle autocompletion score is {middle_autocompletion_score}")
