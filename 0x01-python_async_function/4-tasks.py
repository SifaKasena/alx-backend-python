#!/usr/bin/env python3
"""Defines a coroutine that executes multiple coroutines concurrently."""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    Executes multiple asynchronous tasks concurrently and
    returns their results as they complete.

    Args:
        n (int): The number of tasks to execute.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of results from the completed tasks.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
