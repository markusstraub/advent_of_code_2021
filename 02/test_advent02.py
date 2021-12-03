import more_itertools
from advent02 import (
    get_movement_generator,
    get_position_v1,
    get_position_v2,
)


def test_reader():
    assert more_itertools.ilen(get_movement_generator()) == 6


def test_get_position_v1():
    test_horizontal_v1, test_depth_v1 = get_position_v1(get_movement_generator())
    assert test_horizontal_v1 == 15
    assert test_depth_v1 == 10


def test_get_position_v2():
    test_horizontal_v2, test_depth_v2 = get_position_v2(get_movement_generator())
    assert test_horizontal_v2 == 15
    assert test_depth_v2 == 60
