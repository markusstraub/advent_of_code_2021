import itertools
import more_itertools

test_input = "3,4,3,1,2"


def read_flock(filename=None):
    """return test data if no file is given"""
    line = test_input
    if filename is not None:
        with open(filename) as file:
            line = file.readline().strip()
    return (int(fish) for fish in line.split(","))


def evolve_fish(fish):
    if fish == 0:
        return [6, 8]
    else:
        return [fish - 1]


def evolve_flock(flock, days=1):
    print(f"evolving.. {days} to go")
    # print(f"input flock is {flock}")
    if days == 0:
        yield from flock
    elif days > 0:
        evolved = itertools.chain.from_iterable(map(evolve_fish, flock))
        evolved = list(evolved)
        # print(f"evolve {list(flock)} -> {evolved}")
        yield from evolve_flock(evolved, days=days - 1)
    else:
        raise ValueError(f"unsupported days={days}")


def calc_flock_size(flock):
    return more_itertools.ilen(flock)


if __name__ == "__main__":
    flock_size = calc_flock_size(evolve_flock(read_flock("advent06.txt"), days=80))
    print(f"part1: flock size on day 80 = {flock_size}")

    # this will never finish.. exponential growth
    # flock_size = calc_flock_size(evolve_flock(read_flock("advent06.txt"), days=256))
    # print(f"part2: flock size on day 256 = {flock_size}")
