from django.shortcuts import render
from django.http import HttpResponse
from apps.entrada.forms import EntradaForm
from django.views.generic import ListView
from apps.entrada.models import Entrada
from django_filters.views import FilterView
from django_filters import FilterSet, CharFilter, DateFilter

# class entradaFilter(FilterSet):
#     class Meta:
#         model = Entrada
#         fields = ['dt_entrada', 'id_localidade', 'id_classe']


class entrada(FilterView):
    model = Entrada
    context_object_name = "entradas"
    template_name = "entrada/entrada.html"
    paginate_by = 3


def entrada_cadastro(request):
    form = EntradaForm()
    return render(request, "entrada/entrada_cadastro.html", {'form': form})
