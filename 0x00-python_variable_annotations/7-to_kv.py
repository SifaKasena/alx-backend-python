#!/usr/bin/env python3
"""
Module that takes a string k and an int OR float v as arguments and
returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and a value to a tuple where the value is squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return (k, v * v)
