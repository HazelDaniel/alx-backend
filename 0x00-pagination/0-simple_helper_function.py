#!/usr/bin/env python3
"""this module declares a helper function that takes in
    two integers 'page' and 'page_size' as arguments"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """this function returns a tuple of size 2 containing
        a start index and an end index corresponding to the range of indexes
        to return in a list for those particular pagination parameters"""
    return (max(page - 1, 0) * page_size, page_size * max(page, 1))
