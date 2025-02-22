# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pathlib

import pytest

import aoc24.days.second


@pytest.mark.usefixtures("ray_session")
def test_part_one():
    result = aoc24.days.second.part_one(pathlib.Path("data/2024-12-02.txt.sample"))
    assert result == 2


@pytest.mark.usefixtures("ray_session")
def test_part_two():
    result = aoc24.days.second.part_two(pathlib.Path("data/2024-12-02.txt.sample"))
    assert result == 4
