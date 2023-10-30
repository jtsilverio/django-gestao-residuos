from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.classe.filters import ClasseFilter
from apps.classe.forms import ClasseForm
from apps.classe.models import Classe
from apps.utils.count_active_filters import count_active_filters

PAGESIZE = 15


def classe_index(request):
    page_number = request.GET.get("page")
    model_filter = ClasseFilter(request.GET, queryset=Classe.objects.all())

    query_paginated = Paginator(model_filter.qs, PAGESIZE)
    query_filtered = query_paginated.get_page(page_number)

    context = {
        "object_list": query_filtered,
        "filter_form": model_filter.form,
        "number_of_active_filters": count_active_filters(request, model_filter),
    }
    return render(request, "classe/classe.html", context)


class ClasseCreate(SuccessMessageMixin, CreateView):
    model = Classe
    form_class = ClasseForm
    template_name = "classe/classe_cadastro.html"
    success_message = "Classe cadastrada"
    success_url = reverse_lazy("classe")


class ClasseEdit(SuccessMessageMixin, UpdateView):
    model = Classe
    form_class = ClasseForm
    template_name = "classe/classe_edit.html"
    success_message = "Classe atualizada"
    success_url = reverse_lazy("classe")


def classe_delete(request, pk):
    entry = get_object_or_404(Classe, pk=pk)

    if request.method == "POST":
        entry.delete()
        messages.warning(request, "Classe excluída")

    return redirect("classe")
