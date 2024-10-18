#!/usr/bin/env python3
"""Async Comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing
    over async_generator.

    Returns:
        list[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
