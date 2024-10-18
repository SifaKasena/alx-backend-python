#!/usr/bin/env python3
"""Defines a coroutine that executes multiple coroutines concurrently."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Executes multiple coroutines concurrently and
    returns their results in the order of completion.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of the results of the coroutines.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
