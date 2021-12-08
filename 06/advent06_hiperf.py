import sys
import itertools
import more_itertools

test_input = "3,4,3,1,2"

MAX_AGE = 8


def read_flock(filename=None):
    """return test data if no file is given"""
    line = test_input
    if filename is not None:
        with open(filename) as file:
            line = file.readline().strip()

    flock = {}
    for i in range(MAX_AGE + 1):
        flock[i] = 0
    parsed = [int(fish) for fish in line.split(",")]
    for fish in parsed:
        flock[fish] = flock[fish] + 1
    return flock


def evolve_flock(flock, days=1):
    # print(f"evolving.. {days} to go")
    if days == 0:
        return flock
    elif days > 0:
        new_fish = flock[0]
        for i in range(1, MAX_AGE + 1):
            flock[i - 1] = flock[i]
        flock[6] += new_fish
        flock[MAX_AGE] = new_fish
        return evolve_flock(flock, days=days - 1)
    else:
        raise ValueError(f"unsupported days={days}")


def calc_flock_size(flock):
    return sum(flock.values())


if __name__ == "__main__":
    print(
        f"warning: this script only works for {sys.getrecursionlimit()} days or less (recursion limit!)"
    )

    flock_size = calc_flock_size(evolve_flock(read_flock("advent06.txt"), days=80))
    print(f"part1: flock size on day 80 = {flock_size}")

    flock_size = calc_flock_size(evolve_flock(read_flock("advent06.txt"), days=256))
    print(f"part2: flock size on day 256 = {flock_size}")
