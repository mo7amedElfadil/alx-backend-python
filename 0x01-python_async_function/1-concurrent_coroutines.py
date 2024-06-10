#!/usr/bin/env python3
from typing import List
import asyncio
"""
Let's execute multiple coroutines at the same time with async
Methods:
    wait_random(max_delay: int) -> float: asynchronous coroutine that takes in
    an integer argument that waits for a random delay between 0 and max_delay
    (included and default to 10). Returns the random delay.
    wait_n(n: int, max_delay: int) -> List[float]: asynchronous coroutine that
    takes in 2 integer arguments: n and max_delay. Returns the list of all the
    delays. List will be sorted due to the nature of concurrency.
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for random delays and returns a list of the delays.
    """
    return [await delay
            for delay in asyncio.as_completed([wait_random(max_delay)
                                               for _ in range(n)])]
