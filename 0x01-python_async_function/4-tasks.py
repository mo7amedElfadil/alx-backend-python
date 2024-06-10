#!/usr/bin/env python3
"""
working with async tasks
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for random delays and returns a list of the delays.
    """
    return [await delay
            for delay in asyncio.as_completed([task_wait_random(max_delay)
                                               for _ in range(n)])]
