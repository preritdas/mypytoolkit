"""
General Python-related operations not built into the standard library.
"""
# Non-local imports
import pandas as pd
import numpy as np

# Local imports
from typing import Any


def tprint(arg) -> None:
    """Prints the contents of a variable/object along with its type."""
    print(arg, type(arg))


def closest_value(iterable, value, return_idx=False) -> Any:
    """Returns the index of the closest occurance of
    `value` in `iterable`."""
    differences = list(map(lambda item: abs(value - item), iterable))

    if return_idx:
        return np.argmin(differences)

    return iterable[np.argmin(differences)]


def reverse_dict(dic: dict) -> dict:
    """Reverses the keys and values in a dictionary."""
    # Check that values are single items
    accepted_types = {str, int, float}

    for value in dic.values():
        if type(value) not in accepted_types:
            raise Exception("Dictionary values must be single, immutable objects.")

    return {val: key for key, val in dic.items()}


def remove_nan_df_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes any rows from a DataFrame that contain
    np.nan values. Returns a new DataFrame.
    """
    nan_indexes = []
    for index, row in df.iterrows():
        if any(np.isnan(row)): nan_indexes.append(index)

    return df.drop(labels=nan_indexes)
