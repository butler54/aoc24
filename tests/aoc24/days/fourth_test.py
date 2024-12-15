# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib

import aoc24.days.fourth

def test_part_one(ray_session):
    """"""
    result = aoc24.days.fourth.part_one(pathlib.Path('data/2024-12-04-a.txt.sample'))
    assert result == 18


def test_part_two(ray_session):
    result = aoc24.days.fourth.part_two(pathlib.Path('data/2024-12-03-b.txt.sample'))
    assert result == 0