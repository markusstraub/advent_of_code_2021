from advent10 import (
    read_input,
    calc_corruption_score,
    calc_autocompletion_score,
    calc_middle_autocompletion_score,
)


def test_calc_corruption_score():
    assert calc_corruption_score(")") == 3
    assert calc_corruption_score("())") == 3
    assert calc_corruption_score("]") == 57
    assert calc_corruption_score("()]") == 57
    assert calc_corruption_score("}") == 1197
    assert calc_corruption_score("()}") == 1197
    assert calc_corruption_score(">") == 25137
    assert calc_corruption_score("()>") == 25137


def test_calc_corruption_score_for_test_input():
    assert sum([calc_corruption_score(nav_line) for nav_line in read_input()]) == 26397


def test_calc_autocompletion_score():
    assert calc_autocompletion_score("[({(<(())[]>[[{[]{<()<>>") == 288957
    # complete by adding }}]])})]


def test_calc_middle_autocompletion_score():
    assert calc_middle_autocompletion_score() == 288957
