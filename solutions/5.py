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

    def get_line_coords(self) -> List[Coord]:
        if self.is_horizontal():
            return [Coord(x, self.start.y) for x in range(self.start.x, self.finish.x + 1)]
        if self.is_vertical():
            return [Coord(self.start.x, y) for y in range(self.start.y, self.finish.y + 1)]

    def is_horizontal(self) -> bool:
        return self.start.y == self.finish.y

    def is_vertical(self) -> bool:
        return self.start.x == self.finish.x

    def __bool__(self) -> bool:
        if self.start.x == self.finish.x or self.start.y == self.finish.y:
            return True
        return False


with get_input(__file__) as _input:
    vent_vectors: List[VentVector] = []
    for line in _input:
        coord_strings = [coords.strip() for coords in line.split("->")]
        coord_strings = [Coord(*coord.split(",")) for coord in coord_strings]
        vent = VentVector(*coord_strings)
        if vent:
            vent_vectors.append(VentVector(*coord_strings))

array = np.zeros((1000, 1000))

for vent in vent_vectors:
    for coord in vent.get_line_coords():
        array[coord.x, coord.y] += 1

print(len(np.argwhere(array >= 2)))
