"""
General Python-related operations not built into the standard library.
"""
# Non-local imports
import pandas as pd
import numpy as np

# Local imports
from typing import Any, Iterable, Type, Union


def tprint(arg) -> Union[Any, Type]:
    """Prints the contents of a variable/object along with its type."""
    print(arg, type(arg))
    return arg, type(arg)


def closest_value(iterable: Iterable, value: Any, return_idx=False) -> Any:
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


def reorder_dict(order: list, dic: dict) -> dict:
    """
    Reorders the dictionary according the list of values.
    If there are keys in the dictionary not included in `order`, they
    are included at the end of the dictionary in their original order.
    """
    if not all(key in dic for key in order):
        raise ValueError("Key given in order that's not present in the dict.")

    original_keys = list(dic.keys())
    remainder = original_keys
    for key in order: remainder.remove(key)

    return_dict = {key: dic[key] for key in order}
    for key in remainder:
        return_dict[key] = dic[key]
    
    return return_dict


def remove_nan_df_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes any rows from a DataFrame that contain
    np.nan values. Returns a new DataFrame.
    """
    nan_indexes = []
    for index, row in df.iterrows():
        if any(np.isnan(row)): nan_indexes.append(index)

    return df.drop(labels=nan_indexes)
