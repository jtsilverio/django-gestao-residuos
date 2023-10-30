from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from apps.saida.filters import SaidaFilter
from apps.saida.forms import SaidaForm
from apps.saida.models import Saida
from apps.utils import count_active_filters


def saida_index(request):
    page_number = request.GET.get("page")
    saida_filter = SaidaFilter(request.GET, queryset=Saida.objects.all())

    saida_paginated = Paginator(saida_filter.qs, settings.PAGESIZE)
    saida = saida_paginated.get_page(page_number)

    context = {
        "object_list": saida,
        "filter_form": saida_filter.form,
        "number_of_active_filters": count_active_filters(request, saida_filter),
    }
    return render(request, "saida/saida.html", context)


class SaidaEdit(SuccessMessageMixin, UpdateView):
    model = Saida
    form_class = SaidaForm
    template_name = "saida/saida_edit.html"
    success_message = "Saída atualizada"
    success_url = reverse_lazy("saida")


def saida_cadastro(request):
    if request.method == "POST":
        form = SaidaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Saída cadastrada")
            return HttpResponseRedirect(reverse("saida_cadastro"))
        else:
            messages.error(request, "Erro ao salvar")
    else:
        form = SaidaForm()

    return render(request, "saida/saida_cadastro.html", {"form": form})


def saida_delete(request, pk):
    saida = get_object_or_404(Saida, pk=pk)

    if request.method == "POST":
        saida.delete()
        messages.warning(request, "Saída excluída")

    return redirect("saida")
