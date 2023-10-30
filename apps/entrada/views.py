from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from apps.entrada.filters import EntradaFilter
from apps.entrada.forms import EntradaForm
from apps.entrada.models import Entrada
from apps.utils import count_active_filters

PAGESIZE = 15


def entrada_index(request):
    page_number = request.GET.get("page")
    entradas_filter = EntradaFilter(request.GET, queryset=Entrada.objects.all())

    entradas_paginated = Paginator(entradas_filter.qs, PAGESIZE)
    entradas = entradas_paginated.get_page(page_number)

    context = {
        "object_list": entradas,
        "filter_form": entradas_filter.form,
        "number_of_active_filters": count_active_filters(request, entradas_filter),
    }
    return render(request, "entrada/entrada.html", context)


class EntradaEdit(SuccessMessageMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = "entrada/entrada_edit.html"
    success_message = "Entrada atualizada"
    success_url = reverse_lazy("entrada")


def entrada_cadastro(request):
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada salva com sucesso")
            return HttpResponseRedirect(reverse("entrada_cadastro"))
        else:
            messages.error(request, "Erro ao salvar")
    else:
        form = EntradaForm()

    return render(request, "entrada/entrada_cadastro.html", {"form": form})


def delete_cadastro(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)

    if request.method == "POST":
        entrada.delete()
        messages.warning(request, "Entrada excluída com sucesso")

    return redirect("entrada")
