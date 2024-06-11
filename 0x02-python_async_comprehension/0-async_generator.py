#!/usr/bin/env python3
"""
0. Async Generator
Coroutines can be executed concurrently using the asyncio module in Python.
This allows for concurrent execution of coroutines, which can be used to
parallelize I/O-bound tasks. In this task, we will implement an async
generator called async_generator that takes in an integer n and yields
a random number between 0 and 10 n times.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine will yield a random number between 0 and 10 n times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
