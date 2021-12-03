#%%
import itertools
import more_itertools

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

#%%


def get_movement_tuple(string):
    tokens = string.split(sep=" ")
    return (tokens[0], int(tokens[1]))


def get_movement_generator(file=None):
    """returns test data if no file is given"""
    if file is None:
        return (get_movement_tuple(line) for line in test_input.split(sep="\n"))
    return (get_movement_tuple(line) for line in open(file))


def get_position_v1(movements, start_horizontal=0, start_depth=0):
    horizontal = start_horizontal
    depth = start_depth
    for direction, units in movements:
        if direction == "forward":
            horizontal += units
        elif direction == "down":
            depth += units
        elif direction == "up":
            depth -= units
        else:
            raise ValueError(f"unknown movement direction: {direction}")
    return (horizontal, depth)


def get_position_v2(movements, start_horizontal=0, start_depth=0, start_aim=0):
    horizontal = start_horizontal
    depth = start_depth
    aim = start_aim
    for direction, units in movements:
        if direction == "forward":
            horizontal += units
            depth += (aim * units)
        elif direction == "down":
            aim += units
        elif direction == "up":
            aim -= units
        else:
            raise ValueError(f"unknown movement direction: {direction}")
    return (horizontal, depth)


print(list(get_movement_generator()))
# %%
# our "unit tests"
assert more_itertools.ilen(get_movement_generator()) == 6

test_horizontal_v1, test_depth_v1 = get_position_v1(get_movement_generator())
assert test_horizontal_v1 == 15
assert test_depth_v1 == 10

test_horizontal_v2, test_depth_v2 = get_position_v2(get_movement_generator())
assert test_horizontal_v2 == 15
assert test_depth_v2 == 60
# %%

horizontal_v1, depth_v1 = get_position_v1(get_movement_generator("advent02.txt"))
print(
    f"v1: the subway moved {horizontal_v1} horizontal and {depth_v1} depth",
    f"(multiplied that's {horizontal_v1 * depth_v1})",
)

horizontal_v2, depth_v2 = get_position_v2(get_movement_generator("advent02.txt"))
print(
    f"v2: the subway moved {horizontal_v2} horizontal and {depth_v2} depth",
    f"(multiplied that's {horizontal_v2 * depth_v2})",
)
# %%

# %%
