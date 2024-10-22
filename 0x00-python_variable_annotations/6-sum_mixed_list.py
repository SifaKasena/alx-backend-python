#!/usr/bin/env python3
"""Module that defines sum_mixed_list function with type annotations."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst: The list of integers and floats to sum.

    Returns:
        float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
