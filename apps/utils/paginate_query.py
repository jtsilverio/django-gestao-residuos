from django.core.paginator import Paginator


def paginate_query(request, query, page_size):
    page_number = request.GET.get("page")
    query_paginated = Paginator(query, page_size)
    return query_paginated.get_page(page_number)
