#!/usr/bin/env python3
"""Module that performs type checking"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a zoomed-in version of the input tuple by
    repeating each element a specified number of times.

    Args:
        lst (Tuple): The input tuple to be zoomed in.
        factor (int, optional): The number of times each element
        in the tuple should be repeated. Defaults to 2.

    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
