def count_active_filters(request, form):
    active_filters = []
    for field in request.GET.items():
        if field[0] != "page" and field[0] in form.data.keys() and field[1] != "":
            active_filters.append(field[0])

    return len(active_filters)
