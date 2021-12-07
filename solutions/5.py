from dataclasses import dataclass
from typing import List

import numpy as np

from config import get_input


@dataclass
class Coord:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)


@dataclass
class VentVector:
    start: Coord
    finish: Coord
    part: int

    def get_line_coords(self) -> List[Coord]:
        x_lower, x_higher = sorted((self.start.x, self.finish.x))
        y_lower, y_higher = sorted((self.start.y, self.finish.y))
        if self.is_horizontal():
            return [Coord(x, self.start.y) for x in range(x_lower, x_higher + 1)]
        elif self.is_vertical():
            return [Coord(self.start.x, y) for y in range(y_lower, y_higher + 1)]
        elif self.is_diagonal():
            rise = self.finish.y - self.start.y
            run = self.finish.x - self.start.x
            mag = abs(rise)
            rise_unit = rise / mag
            run_unit = run / mag
            return [
                Coord(self.start.x + (i * run_unit), self.start.y + (i * rise_unit))
                for i in range(mag + 1)
            ]

    def is_horizontal(self) -> bool:
        return self.start.y == self.finish.y

    def is_vertical(self) -> bool:
        return self.start.x == self.finish.x

    def is_diagonal(self) -> bool:
        rise = abs(self.finish.y - self.start.y)
        run = abs(self.finish.x - self.start.x)
        return rise == run

    def __bool__(self) -> bool:
        if self.is_vertical() or self.is_horizontal():
            return True
        elif self.part == 2 and self.is_diagonal():
            return True
        return False


with get_input(__file__) as _input:
    vent_vectors_p1: List[VentVector] = []
    vent_vectors_p2: List[VentVector] = []
    for line in _input:
        coord_strings = [coords.strip() for coords in line.split("->")]
        coord_strings = [Coord(*coord.split(",")) for coord in coord_strings]
        vent_p1 = VentVector(*coord_strings, part=1)
        if vent_p1:
            vent_vectors_p1.append(vent_p1)
        vent_p2 = VentVector(*coord_strings, part=2)
        if vent_p2:
            vent_vectors_p2.append(vent_p2)

array_p1 = np.zeros((1000, 1000))
array_p2 = np.zeros((1000, 1000))

for vent in vent_vectors_p1:
    for coord in vent.get_line_coords():
        array_p1[coord.x, coord.y] += 1

for vent in vent_vectors_p2:
    for coord in vent.get_line_coords():
        array_p2[coord.x, coord.y] += 1

print(" --- Part One --- ")
print(len(np.argwhere(array_p1 > 1)))
print(" --- Part Two --- ")
print(len(np.argwhere(array_p2 > 1)))
