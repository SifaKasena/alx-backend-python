#!/usr/bin/env python3
"""
Module that takes a float n as argument and returns
a function that multiplies a float by n
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by n.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies a float by n.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
