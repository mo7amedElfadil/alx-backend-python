#!/usr/bin/env python3
"""
This module contains a function that takes an iterable of sequences and
returns a list of tuples, each containing an element and its length.
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element and its length.
    """
    return [(i, len(i)) for i in lst]
