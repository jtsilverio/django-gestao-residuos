from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.agua.filters import AguaFilter
from apps.agua.forms import AguaForm
from apps.agua.models import Agua
from apps.utils import count_active_filters

PAGESIZE = 15


def agua_index(request):
    page_number = request.GET.get("page")
    model_filter = AguaFilter(request.GET, queryset=Agua.objects.all())

    query_paginated = Paginator(model_filter.qs, PAGESIZE)
    query_filtered = query_paginated.get_page(page_number)

    context = {
        "object_list": query_filtered,
        "filter_form": model_filter.form,
        "number_of_active_filters": count_active_filters(request, model_filter),
    }
    return render(request, "agua/agua.html", context)


class AguaCreate(SuccessMessageMixin, CreateView):
    model = Agua
    form_class = AguaForm
    template_name = "agua/agua_cadastro.html"
    success_message = "Consumo de Água cadastrado"
    success_url = reverse_lazy("agua")
