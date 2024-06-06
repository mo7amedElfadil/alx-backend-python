#!/usr/bin/env python3
"""
Complex types module - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the first element of the tuple being the string
    and the second square of the number
    """
    return (k, v**2)
