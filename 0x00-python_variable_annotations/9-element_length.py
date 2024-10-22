#!/usr/bin/env python3
"""
Module that takes a list lst as argument and
returns the length of the list
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each string in a list.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
        a string from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
