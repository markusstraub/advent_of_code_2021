import more_itertools
from advent01 import (
    get_rolling_window_increase_count,
    get_sonar_sweep_generator,
    get_increase_count,
)


def test_reader():
    assert more_itertools.ilen(get_sonar_sweep_generator()) == 10


def test_get_increase_count():
    assert get_increase_count(get_sonar_sweep_generator()) == 7


def test_get_rolling_window_increase_count():
    assert get_rolling_window_increase_count() == 5
