from advent11 import Point, EnergyMap


def test_read():
    energy_map = EnergyMap()
    assert energy_map.height == 10
    assert energy_map.width == 10
    assert energy_map.get(Point(0, 0)) == 5
    assert energy_map.get(Point(2, 6)) == 7


def test_neighobrs():
    energy_map = EnergyMap()
    assert len(energy_map.calc_neighbors(Point(0, 0))) == 3
    assert len(energy_map.calc_neighbors(Point(9, 9))) == 3
    assert len(energy_map.calc_neighbors(Point(5, 2))) == 8


def test_simulation():
    assert EnergyMap().simulate(steps=1) == 0
    assert EnergyMap().simulate(steps=2) == 35
    assert EnergyMap().simulate(steps=10) == 204
