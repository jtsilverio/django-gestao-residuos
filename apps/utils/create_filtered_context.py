from .count_active_filters import count_active_filters


def create_filtered_context(query_filtered, model_filter, request):
    return {
        "object_list": query_filtered,
        "filter_form": model_filter.form,
        "number_of_active_filters": count_active_filters(request, model_filter),
    }
