#!/usr/bin/env python3
"""
This script measures the runtime of the async comprehension function
`async_comprehension` four times in parallel using `asyncio.gather`.
"""
from asyncio import gather
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of async_comprehension four times in parallel.
    """
    start_time: float = time.time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    end_time: float = time.time()
    return end_time - start_time
