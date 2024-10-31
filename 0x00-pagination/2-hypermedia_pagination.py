#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import math
from typing import List

""" calculate the start and end indices for a given page and page_size"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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
        return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        if page <= total_pages:
            start, end = index_range(page, page_size)
            return self.dataset()[start:end]
        else:
            return []
        
    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        if page > total_pages:
            return {
                "page_size": page_size,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
            }
        
        start, end = index_range(page, page_size)
        paginated = self.dataset()[start:end]      

        metadata = {
            "page_size": page_size,
            "page": page,
            "data": paginated,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        
        return metadata