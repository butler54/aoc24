# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib
from typing import Annotated, Optional

import num2words
import ray
import typer
from rich import print

import aoc24.days.first
import aoc24.days.fourth
import aoc24.days.second
import aoc24.days.third
import aoc24.days.sixth
from aoc24.__about__ import __version__


def cli():
    """Wrapper CLI command"""
    typer.run(run)

def result(day: int):

    match day:
        case 1:
            print(f'Part 1 result: {aoc24.days.first.part_a(pathlib.Path('data/2024-12-01-a.txt'))}')
            print(f'Part 2 result: {aoc24.days.first.part_b(pathlib.Path('data/2024-12-01-a.txt'))}')

        case 2:
            print(f'Part 1 result: {aoc24.days.second.part_one(pathlib.Path('data/2024-12-02.txt'))}')
            print(f'Part 2 result: {aoc24.days.second.part_two(pathlib.Path('data/2024-12-02.txt'))}')
        case 3:
            print(f'Part 1 result: {aoc24.days.third.part_one(pathlib.Path('data/2024-12-03.txt'))}')
            print(f'Part 2 result: {aoc24.days.third.part_two(pathlib.Path('data/2024-12-03.txt'))}')
        case 4:
            print(f'Part 1 result: {aoc24.days.fourth.part_one(pathlib.Path('data/2024-12-04-a.txt'))}')
            print(f'Part 2 result: {aoc24.days.fourth.part_two(pathlib.Path('data/2024-12-04-a.txt'))}')
        case 6:
            print(f'Part 1 result: {aoc24.days.sixth.part_one(pathlib.Path('data/2024-12-06.txt'))}')
        case _:
            return Null

def run(day: Annotated[int, typer.Argument(help= "which day to pick")]):
    ray.init()
    print(f'Running the {num2words.num2words(day, to='ordinal_num')} days experiment')
    result(day)
    ray.shutdown()


