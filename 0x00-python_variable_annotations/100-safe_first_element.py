#!/usr/bin/env python3
"""
duck typing - first element of a sequence safe from edge cases

"""
from typing import Union, Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element: returns the first element of a sequence
    """
    if lst:
        return lst[0]
    else:
        return None
