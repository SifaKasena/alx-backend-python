#!/usr/bin/env python3
"""Measure Runtime"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of async_comprehension 4 times in parallel.

    Returns:
        float: The total runtime for all four calls to async_comprehension.
    """
    import time
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start
