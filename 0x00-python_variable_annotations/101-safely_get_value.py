#!/usr/bin/env python3
"""Module that takes an iterable object and returns its first element"""
from typing import Union, Any, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value of a key in a dictionary if it exists,
    otherwise returns a default value.

    Args:
        dct (dict): The dictionary from which to retrieve the value.
        key (Any): The key to look for in the dictionary.
        default (Union[TypeVar('T'), None]): The default value to return if
        the key does not exist in the dictionary.

    Returns:
        Union[Any, TypeVar('T')]: The value of the key in the dictionary if it
        exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
