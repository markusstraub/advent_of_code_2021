#%%
import more_itertools
from collections import namedtuple

Point = namedtuple("Point", "x y height")


class HeightMap:
    def __init__(self, height_map):
        self.height_map = height_map
        self.y_count = len(self.height_map)
        self.x_count = len(self.height_map[0])

    def is_in_bounds(self, x, y):
        return x >= 0 and x < self.x_count and y >= 0 and y < self.y_count

    def get(self, x, y):
        if not self.is_in_bounds(x, y):
            return None
        return self.height_map[y][x]

    def get_neighbor_heights(self, x, y):
        neighbors = []
        neighbors.append(self.get(x, y - 1))
        neighbors.append(self.get(x, y + 1))
        neighbors.append(self.get(x + 1, y))
        neighbors.append(self.get(x - 1, y))
        # print(f"neighbors of {x}/{y}: {neighbors}")
        return list(filter(lambda height: height != None, neighbors))

    def is_lowpoint(self, point):
        return self.is_lowpoint_xy(point.x, point.y)

    def is_lowpoint_xy(self, x, y):
        height = self.get(x, y)
        if height is None:
            return None

        larger_neighbors = filter(
            lambda v: v <= height, self.get_neighbor_heights(x, y)
        )
        return len(list(larger_neighbors)) == 0

    def __iter__(self):
        for x in range(self.x_count):
            for y in range(self.y_count):
                yield Point(x, y, self.get(x, y))

    def __str__(self):
        rows_for_printing = []
        for row in self.height_map:
            rows_for_printing.append("".join([str(h) for h in row]))
        return "\n".join(rows_for_printing)


def read_heightmap(filename="test_advent09.txt"):
    """return test data if no file is given"""
    height_map = []
    with open(filename) as file:
        for line in file:
            height_map.append([int(h) for h in line.strip()])
    return HeightMap(height_map)


height_map = read_heightmap()
print(height_map)

lowpoints = list(filter(lambda point: height_map.is_lowpoint(point), height_map))
total_risk = sum([point.height + 1 for point in lowpoints])
print(f"part1: total risk level of {len(lowpoints)} low points is {total_risk}")
# print(list(lowpoints))


# %%

# %%
