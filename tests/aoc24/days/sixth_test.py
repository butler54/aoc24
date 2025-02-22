# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pathlib

import aoc24.days.sixth


def test_part_one(ray_session):
    """"""
    result = aoc24.days.sixth.part_one(pathlib.Path('data/2024-12-06.txt.sample'))
    assert result == 41
