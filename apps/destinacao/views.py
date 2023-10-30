from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.destinacao.filters import DestinacaoFilter
from apps.destinacao.forms import DestinacaoForm
from apps.destinacao.models import Destinacao
from apps.utils.count_active_filters import count_active_filters

PAGESIZE = 15


def destinacao_index(request):
    page_number = request.GET.get("page")
    model_filter = DestinacaoFilter(request.GET, queryset=Destinacao.objects.all())

    query_paginated = Paginator(model_filter.qs, PAGESIZE)
    query_filtered = query_paginated.get_page(page_number)

    context = {
        "object_list": query_filtered,
        "filter_form": model_filter.form,
        "number_of_active_filters": count_active_filters(request, model_filter),
    }
    return render(request, "destinacao/destinacao.html", context)


class DestinacaoCreate(SuccessMessageMixin, CreateView):
    model = Destinacao
    form_class = DestinacaoForm
    template_name = "destinacao/destinacao_cadastro.html"
    success_message = "Tipo de destinação cadastrada"
    success_url = reverse_lazy("destinacao")


class DestinacaoEdit(SuccessMessageMixin, UpdateView):
    model = Destinacao
    form_class = DestinacaoForm
    template_name = "destinacao/destinacao_edit.html"
    success_message = "Tipo de destinação atualizada"
    success_url = reverse_lazy("destinacao")


def destinacao_delete(request, pk):
    entry = get_object_or_404(Destinacao, pk=pk)

    if request.method == "POST":
        entry.delete()
        messages.warning(request, "Tipo de destinação excluída")

    return redirect("destinacao")
