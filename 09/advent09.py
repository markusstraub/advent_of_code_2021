from collections import namedtuple

Point = namedtuple("Point", "x y height")


class HeightMap:
    def __init__(self, height_map):
        self.height_map = height_map
        self.y_count = len(self.height_map)
        self.x_count = len(self.height_map[0])

    def is_in_bounds(self, x, y):
        return x >= 0 and x < self.x_count and y >= 0 and y < self.y_count

    def get_height(self, x, y):
        if not self.is_in_bounds(x, y):
            return None
        return self.height_map[y][x]

    def calc_neighbor_points(self, x, y):
        neighbors = []

        new_points = [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]
        for new_point in new_points:
            new_x, new_y = new_point
            height = self.get_height(new_x, new_y)
            if height != None:
                neighbors.append(Point(new_x, new_y, height))
        return neighbors

    def calc_neighbor_heights(self, x, y):
        return [point.height for point in self.calc_neighbor_points(x, y)]

    def is_lowpoint(self, point):
        return self.is_lowpoint_xy(point.x, point.y)

    def is_lowpoint_xy(self, x, y):
        height = self.get_height(x, y)
        if height is None:
            return None

        larger_neighbors = filter(
            lambda v: v <= height, self.calc_neighbor_heights(x, y)
        )
        return len(list(larger_neighbors)) == 0

    def calc_lowpoints(self):
        return list(filter(lambda point: self.is_lowpoint(point), self))

    def calc_total_risk(self):
        return sum([point.height + 1 for point in self.calc_lowpoints()])

    def calc_basin(self, lowpoint):
        basin = set()
        to_expand = [lowpoint]
        while len(to_expand) > 0:
            point = to_expand.pop()
            basin.add(point)
            neighbors = self.calc_neighbor_points(point.x, point.y)
            neighbors = filter(lambda point: point.height < 9, neighbors)
            to_expand.extend(set(neighbors).difference(basin))
        return basin

    def calc_basins(self):
        return [self.calc_basin(lowpoint) for lowpoint in self.calc_lowpoints()]

    def __iter__(self):
        for x in range(self.x_count):
            for y in range(self.y_count):
                yield Point(x, y, self.get_height(x, y))

    def __str__(self):
        rows_for_printing = []
        for row in self.height_map:
            rows_for_printing.append("".join([str(h) for h in row]))
        return "\n".join(rows_for_printing)


def read_height_map(filename="test_advent09.txt"):
    """return test data if no file is given"""
    height_map = []
    with open(filename) as file:
        for line in file:
            height_map.append([int(h) for h in line.strip()])
    return HeightMap(height_map)


if __name__ == "__main__":
    height_map = read_height_map("advent09.txt")
    total_risk = height_map.calc_total_risk()
    print(f"part1: total risk level is {total_risk}")

    m = read_height_map("advent09.txt")
    basin_sizes = sorted([len(basin) for basin in m.calc_basins()], reverse=True)
    multi = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(
        f"part2: the largest basins are of size {basin_sizes[0:3]}, multiplied that's {multi}"
    )
