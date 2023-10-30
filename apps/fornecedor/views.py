from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.fornecedor.filters import FornecedorFilter
from apps.fornecedor.forms import FornecedorForm
from apps.fornecedor.models import Fornecedor
from apps.utils.count_active_filters import count_active_filters

PAGESIZE = 15


def fornecedor_index(request):
    page_number = request.GET.get("page")
    model_filter = FornecedorFilter(request.GET, queryset=Fornecedor.objects.all())

    query_paginated = Paginator(model_filter.qs, PAGESIZE)
    query_filtered = query_paginated.get_page(page_number)

    context = {
        "object_list": query_filtered,
        "filter_form": model_filter.form,
        "number_of_active_filters": count_active_filters(request, model_filter),
    }
    return render(request, "fornecedor/fornecedor.html", context)


class FornecedorCreate(SuccessMessageMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedor/fornecedor_cadastro.html"
    success_message = "Fornecedor cadastrado"
    success_url = reverse_lazy("fornecedor")

    ## make destinacao disabled by default
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["destinacao"].disabled = True
        return form


class FornecedorEdit(SuccessMessageMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedor/fornecedor_edit.html"
    success_message = "Fornecedor atualizado"
    success_url = reverse_lazy("fornecedor")


def fornecedor_delete(request, pk):
    entry = get_object_or_404(Fornecedor, pk=pk)

    if request.method == "POST":
        entry.delete()
        messages.warning(request, "Fornecedor excluído")

    return redirect("classe")
