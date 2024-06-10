#!/usr/bin/env python3
"""Basics of async

This script demonstrates the basic syntax of async and await.
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Given max_delay, wait for a random delay between 0 and max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
