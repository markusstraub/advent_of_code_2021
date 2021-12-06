from advent06_hiperf import read_flock, evolve_flock, calc_flock_size


def test_evolve_flock():
    assert calc_flock_size(evolve_flock(read_flock(), days=1)) == 5
    assert calc_flock_size(evolve_flock(read_flock(), days=18)) == 26
    assert calc_flock_size(evolve_flock(read_flock(), days=80)) == 5934
