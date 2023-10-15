from django.shortcuts import render


# Create your views here.
def combustivel_index(request):
    query_paginated = Paginator(model_filter.qs PAGESIZE)
    return render(request, "combustivel/combustivel.html")

