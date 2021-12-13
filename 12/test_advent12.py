from advent12 import as_new_list, is_small_cave, Caves


def test_is_small_cave():
    assert is_small_cave("small")
    assert not is_small_cave("XXL")


def test_as_new_list():
    one_item = as_new_list("stringi")
    assert len(one_item) == 1
    assert one_item[-1] == "stringi"

    two_items = as_new_list(["stringi", "bingi"])
    assert len(two_items) == 2
    assert two_items[-1] == "bingi"


def test_routing():
    caves = Caves()
    paths = caves.find_all_paths("start", "end")
    assert len(paths) == 10
