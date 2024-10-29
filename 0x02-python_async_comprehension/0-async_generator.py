#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import Generator
from types import NoneType

async def async_generator() -> Generator[float, NoneType, NoneType]:
    """
    An asynchronous generator that yields random numbers.

    This coroutine will asynchronously yield a random float between 0 and 10,
    one at a time, with a 1-second delay between each yield.

    Yields:
        float: A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
