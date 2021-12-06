from advent06 import read_flock, evolve_fish, evolve_flock, calc_flock_size


def test_evolve_fish():
    assert evolve_fish(6) == [5]
    assert evolve_fish(0) == [6, 8]


def test_evolve_micro_flock():
    microflock = [0]
    assert list(evolve_flock(microflock, days=1)) == [6, 8]


def test_evolve_flock():
    flock_day1 = list(evolve_flock(read_flock(), days=1))
    assert flock_day1 == [2, 3, 2, 0, 1]

    flock_day2 = list(evolve_flock(read_flock(), days=2))
    assert flock_day2 == [1, 2, 1, 6, 8, 0]

    flock_day3 = list(evolve_flock(read_flock(), days=3))
    assert flock_day3 == [0, 1, 0, 5, 7, 6, 8]

    assert calc_flock_size(evolve_flock(read_flock(), days=18)) == 26
    assert calc_flock_size(evolve_flock(read_flock(), days=80)) == 5934
