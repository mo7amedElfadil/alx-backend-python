#!/usr/bin/env python3
"""
sum_mixed_list module - sum_mixed_list function.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Sum the elements of a list of integers and floats."""
    return sum(mxd_lst)
