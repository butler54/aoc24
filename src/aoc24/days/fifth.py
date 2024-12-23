# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import pathlib  # noqa: TCH003 (automatically moving here)


def read_file(path: pathlib.Path) -> tuple[list[tuple[int, int]], list[list[int]]]:
    with path.open("r") as f:
        lines = f.readlines()

    tuples = []
    listofints = []
    blank = False
    for line in lines:
        clean = line.strip()
        if clean == "":
            blank = True
        elif blank:
            listofints.append([int(num.strip()) for num in clean.split(",")])
        else:
            nums = clean.split("|")
            tuples.append((int(nums[0]), int(nums[1])))
    return tuples, listofints


def sort(sample: list[int], predicates: list[tuple[int, int]]) -> list[int]:
    changed = True
    while changed:
        changed = False
        for predicate in predicates:
            try:
                l_index = sample.index(predicate[0])
                r_index = sample.index(predicate[1])
                if r_index < l_index:
                    temp = sample[r_index]
                    sample[r_index] = sample[l_index]
                    sample[l_index] = temp
                    changed = True
            except ValueError:
                continue
    return sample


def correctly_sorted(sample: list[int], predicates: list[tuple[int, int]]) -> bool:
    for predicate in predicates:
        try:
            l_index = sample.index(predicate[0])
            r_index = sample.index(predicate[1])
            if r_index < l_index:
                # not sorted correctly
                return False
        except ValueError:
            continue
    return True


def part_one(path: pathlib.Path) -> int:
    tuples, lists = read_file(path)
    sumation = 0
    for line in lists:
        if correctly_sorted(line, tuples):
            sumation += line[int(len(line) / 2)]
    return sumation


def part_two(path: pathlib.Path) -> int:
    tuples, lists = read_file(path)
    sumation = 0
    for line in lists:
        if not correctly_sorted(line, tuples):
            cor_sorted = sort(line, tuples)

            sumation += cor_sorted[int(len(cor_sorted) / 2)]

    return sumation
