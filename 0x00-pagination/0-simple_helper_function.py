#!/usr/bin/env python3
"""
Simple helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that return a starting index and a end index
    Args:
        page: page number
        page_size: number of items per page
    Returns:
        Tuple with start and end index
    """
    return ((page - 1) * page_size, page * page_size)
