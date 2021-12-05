#%%
import itertools
import more_itertools

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

#%%


def read_input(filename=None):
    """return test data if no file is given"""
    if filename is None:
        yield from ((line) for line in test_input.split("\n"))
    else:
        with open(filename) as file:
            for line in file:
                yield line.strip()


def full_range(a, b):
    if a <= b:
        return range(a, b + 1)
    else:
        return range(a, b - 1, -1)


def create_vent_map(filename=None, allow_diagonal=True):
    gen = read_input(filename)
    vent_map = {}
    for line in gen:
        start, stop = line.split(" -> ")
        start_x, start_y = [int(val) for val in start.split(",")]
        stop_x, stop_y = [int(val) for val in stop.split(",")]
        # if start_x > stop_x:
        #    start_x, stop_x = (stop_x, start_x)
        # if start_y > stop_y:
        #    start_y, stop_y = (stop_y, start_y)

        is_diagonal = stop_x != start_x and stop_y != start_y
        if is_diagonal and not allow_diagonal:
            continue
        elif is_diagonal:
            tuples = zip(full_range(start_x, stop_x), full_range(start_y, stop_y))
            for tuple in tuples:
                current_vents = vent_map.get(tuple)
                if current_vents is None:
                    current_vents = 0
                current_vents += 1
                vent_map[tuple] = current_vents
        else:
            if stop_x != start_x:
                for x in full_range(start_x, stop_x):
                    current_vents = vent_map.get((x, start_y))
                    if current_vents is None:
                        current_vents = 0
                    current_vents += 1
                    vent_map[(x, start_y)] = current_vents

            if stop_y != start_y:
                for y in full_range(start_y, stop_y):
                    current_vents = vent_map.get((start_x, y))
                    if current_vents is None:
                        current_vents = 0
                    current_vents += 1
                    vent_map[(start_x, y)] = current_vents

    return vent_map


def count_danger_areas(vent_map, danger_limit=2):
    danger_count = 0
    for vent_count in vent_map.values():
        if vent_count >= danger_limit:
            danger_count += 1
    return danger_count


def print_vent_map(vent_map):
    max_x = max([x for x, y in vent_map.keys()])
    max_y = max([y for x, y in vent_map.keys()])
    print(" " + "-" * max_x)
    for y in range(0, max_x + 1):
        print("|", end="")
        for x in range(0, max_y + 1):
            value = vent_map.get((x, y))
            if value is None:
                value = "."
            print(value, end="")
        print("|")
    print(" " + "-" * max_x)


if __name__ == "__main__":
    print("test map without diagonal vents:")
    print_vent_map(create_vent_map(allow_diagonal=False))
    print("test map with diagonal vents:")
    print_vent_map(create_vent_map(allow_diagonal=True))

    vent_map_no_diagonal = create_vent_map(
        filename="advent05.txt", allow_diagonal=False
    )
    vent_map = create_vent_map(filename="advent05.txt", allow_diagonal=True)
    danger_limit = 2
    danger_count_no_diagonal = count_danger_areas(
        vent_map_no_diagonal, danger_limit=danger_limit
    )
    print(
        f"part1: found {danger_count_no_diagonal} dangerous vent crossings (>{danger_limit} vents, no diagonal vents)"
    )
    danger_count = count_danger_areas(vent_map, danger_limit=danger_limit)
    print(
        f"part2: found {danger_count} dangerous vent crossings (>{danger_limit} vents)"
    )


# %%
