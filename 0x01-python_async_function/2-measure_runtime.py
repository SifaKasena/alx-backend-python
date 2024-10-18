#!/usr/bin/env python3
"""Define measure_time function"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing wait_n function.

    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay for each wait_n call.

    Returns:
        float: The average runtime per execution of wait_n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
