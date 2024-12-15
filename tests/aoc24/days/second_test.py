# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pathlib

import aoc24.days.second





def test_part_one(ray_session):
    result = aoc24.days.second.part_one(pathlib.Path('data/2024-12-02.txt.sample'))
    assert result == 2

def test_part_two(ray_session):
    result = aoc24.days.second.part_two(pathlib.Path('data/2024-12-02.txt.sample'))
    assert result == 4