# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib

import aoc24.days.fourth


<<<<<<< HEAD
def test_part_one(ray_session):
=======
def test_part_one():
>>>>>>> main
    """"""
    result = aoc24.days.fourth.part_one(pathlib.Path("data/2024-12-04-a.txt.sample"))
    assert result == 18


<<<<<<< HEAD
def test_part_two(ray_session):
    result = aoc24.days.fourth.part_two(pathlib.Path('data/2024-12-04-a.txt.sample'))
=======
def test_part_two():
    result = aoc24.days.fourth.part_two(pathlib.Path("data/2024-12-04-a.txt.sample"))
>>>>>>> main
    assert result == 9
