#!/usr/bin/env python3
"""Module that takes an iterable object and returns its first element"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): The sequence from which to retrieve
        the first element.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
