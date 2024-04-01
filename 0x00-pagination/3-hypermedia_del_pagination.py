#!/usr/bin/env python3
"""Task 3: Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """this function returns a tuple of size 2 containing
        a start index and an end index corresponding to the range of indexes
        to return in a list for those particular pagination parameters"""
    return (max(page - 1, 0) * page_size, page_size * max(page, 1))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ ACached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data and performs some
            assertions on the page and page_size """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves info about a page from a given index and with a
        specified size.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        page_data = []
        data_count = 0
        next_index = None
        start_index = index if index else 0

        for i, item in data.items():
            if i >= start_index and data_count < page_size:
                page_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = i
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
