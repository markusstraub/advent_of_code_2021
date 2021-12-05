from advent05 import full_range, create_vent_map, count_danger_areas


def test_full_range():
    assert list(full_range(0, 2)) == [0, 1, 2]
    assert list(full_range(5, 3)) == [5, 4, 3]


def test_only_straight_vents():
    vent_map = create_vent_map(allow_diagonal=False)
    danger_limit = 2
    danger_count = count_danger_areas(vent_map, danger_limit=danger_limit)
    assert danger_count == 5


def test_vents():
    vent_map = create_vent_map(allow_diagonal=True)
    danger_limit = 2
    danger_count = count_danger_areas(vent_map, danger_limit=danger_limit)
    assert danger_count == 12
