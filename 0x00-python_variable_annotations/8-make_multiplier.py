#!/usr/bin/env python3
"""
callable function that multiplies a float by a given multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def multiplier_func(number: float) -> float:
        """ Returns number multiplied by multiplier """
        return number * multiplier
    return multiplier_func
