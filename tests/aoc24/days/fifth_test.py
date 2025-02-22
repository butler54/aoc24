# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib

import aoc24.days.fifth


def test_part_one():
    """"""
    result = aoc24.days.fifth.part_one(pathlib.Path("data/2024-12-05.txt.sample"))
    assert result == 143


def test_part_two():
    """"""
    result = aoc24.days.fifth.part_two(pathlib.Path("data/2024-12-05.txt.sample"))
    assert result == 123


def test_read():
    tuples, listofints = aoc24.days.fifth.read_file(pathlib.Path("data/2024-12-05.txt.sample"))

    assert tuples[0][0] == 47
    assert tuples[1][1] == 13
    assert listofints[0][0] == 75
    assert listofints[1][1] == 61
