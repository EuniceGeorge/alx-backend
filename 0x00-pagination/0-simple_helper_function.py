#!/usr/bin/env python3
""" function"""

def index_range(page, page_size):
    """ index_range"""
    start_page = (page-1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)
