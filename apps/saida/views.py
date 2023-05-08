from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.core.paginator import Paginator

from apps.saida.filters import SaidaFilter
from apps.saida.models import Saida

PAGESIZE = 15

def saida_index(request):
    page_number = request.GET.get("page")
    saida_filter = SaidaFilter(request.GET,
                             queryset=Saida.objects.all())
    
    saida_paginated = Paginator(saida_filter.qs, PAGESIZE)
    saida = saida_paginated.get_page(page_number)
    
    context = {
        "object_list": saida,
        "filter_form": saida_filter.form,
    }
    return render(request, "saida/saida.html", context)
