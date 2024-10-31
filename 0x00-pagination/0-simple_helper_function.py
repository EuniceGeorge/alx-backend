#!/usr/bin/env python3
"""function"""


def index_range(page, page_size):
    """ index_range"""
    start = (page-1) * page_size
    end = start + page_size
    return (start, end)
