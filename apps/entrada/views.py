from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from apps.entrada.forms import EntradaForm
from django.views.generic import ListView
from apps.entrada.models import Entrada
from django_filters.views import FilterView
from django_filters import FilterSet, CharFilter, DateFilter
from django.contrib import messages
from django.shortcuts import redirect

# class entradaFilter(FilterSet):
#     class Meta:
#         model = Entrada
#         fields = ['dt_entrada', 'id_localidade', 'id_classe']


class entrada(FilterView):
    model = Entrada
    context_object_name = "entradas"
    template_name = "entrada/entrada.html"
    paginate_by = 20


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
    
    return render(request, "entrada/entrada_cadastro.html", {'form': form})
