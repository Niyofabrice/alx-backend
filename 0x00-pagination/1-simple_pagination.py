#!/usr/bin/env python3
"""
Simple pagination
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function that returns the appropriate page of the dataset
        Args:
            page: page number
            page_size: number of items per page
        Returns:
            List of rows of items
        """
        self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        range = index_range(page, page_size)
        return self.__dataset[range[0]:range[1]]
