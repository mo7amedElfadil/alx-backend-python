#!/usr/bin/env python3
"""
1. Async Comprehensions
Asynchronous Comprehensions in Python are a feature that allows you to create
asynchronous generators in a more concise way.
It is similar to list comprehensions, but it is used to create asynchronous
generators. This means that you can use it to iterate over asynchronous data
and generate asynchronous values.
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Async Generator"""
    result: list[float] = [i async for i in async_generator()]
    return result
