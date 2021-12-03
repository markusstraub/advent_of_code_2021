#%%
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


# %%


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


#%%
# our "unit tests"
assert more_itertools.ilen(get_sonar_sweep_generator()) == 10
assert get_increase_count(get_sonar_sweep_generator()) == 7

#%%

sonar_length = more_itertools.ilen(get_sonar_sweep_generator("advent01.txt"))
sonar_increases = get_increase_count(get_sonar_sweep_generator("advent01.txt"))
print(f"sonar sweep with {sonar_length} samples contains {sonar_increases} increases")

#%% below here is the old approach.. TODO rework the rolling window stuff (why did the generator provided through a function not work properly)

#%%

regular = (line for line in test_input.split())
delayed = itertools.chain([None], (line for line in test_input.split()))

# print(list(map(b_larger_than_a, delayed, regular)))
increases = len(
    list(itertools.filterfalse(lambda x: not x, map(b_larger_than_a, delayed, regular)))
)
print(f"found {increases} increases in file")

# print(list(regular))
# print(list(delayed))


# %%
def get_input():
    return (int(line) for line in test_input.split())


def get_rolling_window(window_size):
    generators = []
    for i in range(0, window_size):
        generators.append(itertools.islice(get_sonar_sweep_generator(), i, None))
    return generators


window_size = 3

print(list(zip(get_rolling_window(window_size))))

for gen in get_rolling_window(window_size):
    print(list(gen))

print(list(get_rolling_window(3)))
# %%
tuples = list(
    zip(
        itertools.islice(get_sonar_sweep_generator(), 0, None),
        itertools.islice(get_input(), 1, None),
        itertools.islice(get_input(), 2, None),
    )
)
print(tuples)
sums = list(map(sum, tuples))
print(sums)

regular = (s for s in sums)
delayed = itertools.chain([None], (s for s in sums))

# print(list(map(b_larger_than_a, delayed, regular)))
increases = len(
    list(itertools.filterfalse(lambda x: not x, map(b_larger_than_a, delayed, regular)))
)
print(f"found {increases} increases in file")
# %%
