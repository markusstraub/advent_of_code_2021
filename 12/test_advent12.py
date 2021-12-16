from advent12 import (
    is_small_cave,
    Caves,
    filter_small_caves_only_once,
    filter_small_caves_only_twice,
)


def test_is_small_cave():
    assert is_small_cave("small")
    assert not is_small_cave("XXL")


def test_as_new_list():
    one_item = list(["stringi"])
    assert len(one_item) == 1
    assert one_item[-1] == "stringi"

    two_items = list(["stringi", "bingi"])
    assert len(two_items) == 2
    assert two_items[-1] == "bingi"


def test_routing_part1():
    caves = Caves()
    paths = caves.find_all_paths("start", "end", filter_small_caves_only_once)
    assert len(paths) == 10


def test_routing_part2():
    caves = Caves()
    paths = caves.find_all_paths("start", "end", filter_small_caves_only_twice)
    assert len(paths) == 36
