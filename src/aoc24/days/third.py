# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pathlib
import re


def part_one(path: pathlib.Path) -> int:
    text = path.read_text()

    result = re.findall(r"mul\((\d+),(\d+)\)", text)
    return sum([int(tup[0]) * int(tup[1]) for tup in result])


def part_two(path: pathlib.Path) -> int:
    text = path.read_text()
    # find the strings
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

    state = 1
    result = 0
    for item in matches:
        if item[0] == "m":
            nums = item[4:-1].split(",")
            result += state * int(nums[0]) * int(nums[1])
        elif item[2] == "(":
            state = 1
        elif item[2] == "n":
            state = 0
        else:
            msg = "WTF"
            raise Exception(msg)  # noqa: TRY002 can't be bothered
    return result
