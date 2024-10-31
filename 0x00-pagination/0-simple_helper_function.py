def index_range(page, page_size):
    start_page = (page-1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)