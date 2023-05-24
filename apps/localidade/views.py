from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.localidade.filters import LocalidadeFilter
from apps.localidade.forms import LocalidadeForm
from apps.localidade.models import Localidade
from apps.utils import count_active_filters

PAGESIZE = 15


def localidade_index(request):
    page_number = request.GET.get("page")
    model_filter = LocalidadeFilter(request.GET, queryset=Localidade.objects.all())

    query_paginated = Paginator(model_filter.qs, PAGESIZE)
    query_filtered = query_paginated.get_page(page_number)

    context = {
        "object_list": query_filtered,
        "filter_form": model_filter.form,
        "number_of_active_filters": count_active_filters(request, model_filter),
    }
    return render(request, "localidade/localidade.html", context)


class LocalidadeEdit(SuccessMessageMixin, UpdateView):
    model = Localidade
    form_class = LocalidadeForm
    template_name = "localidade/localidade_edit.html"
    success_message = "Localidade atualizada"
    success_url = reverse_lazy("localidade")


# use generic view to create a page for entering new localidade
class LocalidadeCreate(SuccessMessageMixin, CreateView):
    model = Localidade
    form_class = LocalidadeForm
    template_name = "localidade/localidade_cadastro.html"
    success_message = "Localidade cadastrada"
    success_url = reverse_lazy("localidade")


def localidade_delete(request, pk):
    localidade = get_object_or_404(Localidade, pk=pk)

    if request.method == "POST":
        localidade.delete()
        messages.warning(request, "Localidade excluída")

    return redirect("localidade")
