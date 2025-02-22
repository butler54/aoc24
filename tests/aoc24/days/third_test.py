# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib

import aoc24.days.third


def test_part_one():
    """"""
    result = aoc24.days.third.part_one(pathlib.Path("data/2024-12-03.txt.sample"))
    assert result == 161


def test_part_two():
    """"""
    result = aoc24.days.third.part_two(pathlib.Path("data/2024-12-03-b.txt.sample"))
    assert result == 48
