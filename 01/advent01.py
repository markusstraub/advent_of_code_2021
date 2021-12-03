import itertools
import more_itertools


test_input = """199
200
208
210
200
207
240
269
260
263"""


def get_sonar_sweep_generator(file=None):
    """returns test data if no file is given"""
    if file is None:
        return (int(line) for line in test_input.split())
    return (int(line) for line in open(file))


def b_larger_than_a(a, b):
    result = False
    if a is not None and b is not None:
        result = b > a
    # print(f"{b} > {a}? {result}")
    return result


def get_increase_count(sonar_sweep):
    pairs = more_itertools.pairwise(sonar_sweep)
    increases = itertools.starmap(b_larger_than_a, pairs)
    return more_itertools.ilen(itertools.filterfalse(lambda x: not x, increases))


def get_rolling_window_generators(file, window_size):
    generators = []
    for i in range(0, window_size):
        generators.append(itertools.islice(get_sonar_sweep_generator(file), i, None))
    return generators


def get_rolling_window_increase_count(file=None, window_size=3):
    """this is really overcomplicated, but I wanted to play with generators"""
    tuples = list(zip(*get_rolling_window_generators(file, window_size)))
    # print(tuples)
    sums = list(map(sum, tuples))
    # print(sums)

    regular = (s for s in sums)
    delayed = itertools.chain([None], (s for s in sums))

    # print(list(map(b_larger_than_a, delayed, regular)))
    increases = len(
        list(
            itertools.filterfalse(
                lambda x: not x, map(b_larger_than_a, delayed, regular)
            )
        )
    )
    return increases


if __name__ == "__main__":
    sonar_length = more_itertools.ilen(get_sonar_sweep_generator("advent01.txt"))
    print(f"using sonar sweep data with {sonar_length} samples.")
    sonar_increases = get_increase_count(get_sonar_sweep_generator("advent01.txt"))
    print(f"part1: sonar sweep found {sonar_increases} increases")

    window_size = 3
    sonar_increases_rolling = get_rolling_window_increase_count(
        file="advent01.txt", window_size=window_size
    )
    print(
        f"part2: sonar sweep found {sonar_increases_rolling} increases (rolling window: {window_size})"
    )
