from advent10 import read_input, check_validity


def test_validity():
    assert check_validity(")") == 3
    assert check_validity("())") == 3
    assert check_validity("]") == 57
    assert check_validity("()]") == 57
    assert check_validity("}") == 1197
    assert check_validity("()}") == 1197
    assert check_validity(">") == 25137
    assert check_validity("()>") == 25137


def test_validity_for_test_input():
    assert sum([check_validity(chunk) for chunk in read_input()]) == 26397
