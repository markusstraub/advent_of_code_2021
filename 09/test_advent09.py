from advent09 import read_height_map


def test_risk_level():
    height_map = read_height_map()
    assert height_map.calc_total_risk() == 15


def test_basins():
    height_map = read_height_map()
    basin_sizes = [len(basin) for basin in height_map.calc_basins()]
    assert set(basin_sizes) == set([3, 9, 9, 14])
