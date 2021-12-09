from advent09 import read_heightmap


def test_risk_level():
    height_map = read_heightmap()
    assert height_map.calc_total_risk() == 15
