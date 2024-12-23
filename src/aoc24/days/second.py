# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib

import modin.pandas as pd
import numpy as np
import numpy.typing as npt


def single_safe(array: npt.NDArray[np.int_]) -> bool:
    diff = array[1:] - array[:-1]
    abs_diff = np.abs(diff)

    if abs(diff.sum()) == abs_diff.sum():
        diff = np.logical_and(np.greater(abs_diff, 0), np.greater(4, abs_diff))
        return diff.all()
    return False


def safe(string: str) -> bool:
    """Return zero or one base on unsafe or safe."""
    return single_safe(np.array(list(map(int, string.split(" ")))))


def drop_safe(string: str) -> bool:
    """See whether safe is still true dropping an element"""
    array = np.array(list(map(int, string.split(" "))))

    if single_safe(array):
        return True
    return any(single_safe(np.delete(array, ii)) for ii in range(array.size))


def part_one(data_path: pathlib.Path) -> int:
    df = pd.read_table(data_path, header=None)
    res = df[0].apply(safe)
    return res.sum()


def part_two(data_path: pathlib.Path) -> int:
    df = pd.read_table(data_path, header=None)
    res = df[0].apply(drop_safe)
    return res.sum()
