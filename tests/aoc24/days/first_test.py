# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0


import pathlib

import aoc24.days.first


def test_first_a(ray_session):
    result = aoc24.days.first.part_a(pathlib.Path('data/2024-12-01-a.txt.sample'))
    assert result == 11


def test_first_b(ray_session):
    result = aoc24.days.first.part_b(pathlib.Path('data/2024-12-01-a.txt.sample'))
    assert result == 31