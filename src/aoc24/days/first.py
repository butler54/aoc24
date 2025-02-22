# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib

import modin.pandas as pd


def sort_series(col: pd.Series) -> pd.Series:
    return col.sort_values(ascending=True).reset_index(drop=True)



def part_a(data_path: pathlib.Path) -> int:
    df = pd.read_table(data_path, sep = r'\s+', header=None)
    new_df = pd.DataFrame({col: sort_series(df[col]) for col in df.columns})
    result = abs(new_df[0] - new_df[1])

    return result.sum()


def part_b(data_path: pathlib.Path) -> int:
    df = pd.read_table(data_path, sep = r'\s+', header=None)
    print(df)
    series = list(df[1])
    print(series)
    df[2] = df.apply(lambda row: series, axis=1) # this doesn't work as the indexing be smart // map
    print(df)
    new = df.apply(lambda x: x[0] * sum(1 for item in x[2] if item == x[0]), axis=1).sum()
    return new
