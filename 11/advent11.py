#%%
import itertools
from collections import namedtuple

MAX_ENERGY = 9
FILENAME = "advent11.txt"
TEST_FILENAME = "test_advent11.txt"


Point = namedtuple("Point", "x y")


class EnergyMap:
    def __init__(self, filename=TEST_FILENAME):
        self._energy = dict()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                for energy in line.strip():
                    self._energy[Point(x, y)] = int(energy)
                    x += 1
                    self._width = x
                y += 1
            self._height = y

    @property
    def height(self):
        """range of y"""
        return self._height

    @property
    def width(self):
        """range of x"""
        return self._width

    def get(self, point):
        return self._energy.get(point)

    def set(self, point, energy):
        self._energy[point] = energy

    def calc_neighbors(self, point):
        deltas = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
        deltas.remove((0, 0))

        neighbors = []
        for delta in deltas:
            new_x = point.x + delta[0]
            new_y = point.y + delta[1]
            if (0 <= new_x < self.width) and (0 <= new_y < self.height):
                neighbors.append(Point(new_x, new_y))
        return neighbors

    def __iter__(self):
        for point in self._energy:
            yield point

    def __str__(self):
        rows = []
        for y in range(self.height):
            rows.append(
                "".join([str(self._energy.get(Point(x, y))) for x in range(self.width)])
            )
        return "\n".join(rows)

    def simulate(self, steps=1):
        """returns nr of flashes that occurred during the simulation"""
        flashes = 0
        for _ in range(steps):
            flashes += self._simulate()
        return flashes

    def _simulate(self, steps=1):
        """returns nr of flashes that occurred during the simulation"""
        for point in self:
            self.set(point, self.get(point) + 1)

        flashed = set()
        new_flashers = set(self._ready_to_flash()).difference(flashed)

        while len(new_flashers) > 0:
            for point in new_flashers:
                flashed.add(point)
                for neighbor in self.calc_neighbors(point):
                    self.set(neighbor, self.get(neighbor) + 1)
            new_flashers = set(self._ready_to_flash()).difference(flashed)

        for point in self._ready_to_flash():
            self.set(point, 0)

        return len(flashed)

    def _ready_to_flash(self):
        return filter(lambda point: self.get(point) > MAX_ENERGY, self)

    def all_octopusses_flashed(self):
        return len(list(filter(lambda point: self.get(point) > 0, self))) == 0


if __name__ == "__main__":
    energy_map = EnergyMap(FILENAME)
    flashes = energy_map.simulate(steps=100)
    print(f"part1: we observed {flashes} flashes")

    energy_map = EnergyMap(FILENAME)
    iteration = 1
    while True:
        energy_map.simulate(steps=1)
        if energy_map.all_octopusses_flashed():
            break
        iteration += 1
    print(
        f"part2: all octopusses flashed during iteration {iteration}. It's safe to go!"
    )


# %%
