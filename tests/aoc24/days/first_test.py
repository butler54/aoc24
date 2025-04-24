# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0


import pathlib

import aoc24.days.first
import pytest


@pytest.mark.usefixtures("ray_session")
def test_first_a():
    result = aoc24.days.first.part_a(pathlib.Path("data/2024-12-01-a.txt.sample"))
    assert result == 11


@pytest.mark.usefixtures("ray_session")
def test_first_b():
    result = aoc24.days.first.part_b(pathlib.Path("data/2024-12-01-a.txt.sample"))
    assert result == 31
