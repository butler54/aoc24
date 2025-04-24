# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import enum
import pathlib

import numpy as np


def part_one(path: pathlib.Path) -> int:
    mapper = MapMover(path)
    return mapper.run()


class Direction(enum.Enum):
    north = [-1, 0]
    south = [1, 0]
    west = [0, -1]
    east = [0, 1]


class StringInterpretationEnum(enum.Enum):
    @classmethod
    def from_str(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"Invalid string value: {value}")


class Cell(StringInterpretationEnum):
    UNVISITED = "."
    VISITED = "X"
    BLOCKED = "#"



class MapMover:

    rotate = np.array([[0, 1], [-1, 0]])
    def __init__(self, path: pathlib.Path):
        with path.open() as f:
            lines = [line.rstrip() for line in f]
        self.rows  = len(lines)
        self.columns = len(lines[0])
        self.array = []

        for row in range(self.rows):
            row_data = []
            for column in range(self.columns):
                try:
                    row_data.append(Cell.from_str(lines[row][column]))
                except ValueError:
                    row_data.append(Cell.VISITED)
                    direction_str = lines[row][column]
                    self.location = np.array([row, column])
                    if direction_str == '^':
                        self.direction = np.array(Direction.north.value)
                    elif direction_str == '>':
                        self.direction = np.array(Direction.east.value)
                    elif direction_str == '<':
                        self.direction = np.array(Direction.west.value)
                    elif direction_str == 'v':
                        self.direction = np.array(Direction.south.value)
            self.array.append(row_data)

    def step(self) -> bool:
        next_loc = self.location + self.direction
        if self.outside(next_loc):
            return True
        next_map = self.array[next_loc[0]][next_loc[1]]

        if next_map == Cell.BLOCKED:
            self.direction = np.dot(self.rotate, self.direction)
        else:
            self.array[next_loc[0]][next_loc[1]] = Cell.VISITED
            self.location = next_loc
        return False


    def temporal_loop(self) -> int:
        self.starting_loc = self.location
        self.ref_array = self.array
        test_step = 0
        unique_locs = 0
        previous_locations = []
        while True:
            pass

            # step through to test step
            # check if next is an existing block, if so skip
            # check if it's in the previous blocks - assume it has to be added first - fi so skip
            # Add the block
            # step until either of the following conditions:
            # exit (in which case it doesn't count)
            # end up in the same block and direction as previously (if so add)




    def outside(self, coord) -> bool:
        if coord[0] < 0:
            return True
        if coord[0] == self.rows:
            return True
        if coord[1] < 0:
            return True
        if coord[1] == self.columns:
            return True

        return False



    def run(self) -> int:
        outside = False
        while not outside:
            outside = self.step()
            print(f'Step, current count {self.count()}')
        return self.count()

    def count(self) -> int:
        count = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.array[row][column] == Cell.VISITED:
                    count = count + 1
        return count
# Example usage:

