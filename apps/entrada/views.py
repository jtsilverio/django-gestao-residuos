from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from apps.entrada.forms import EntradaForm
from apps.entrada.models import Entrada


class entrada(ListView):
    model = Entrada
    context_object_name = "entradas"
    template_name = "entrada/entrada.html"
    paginate_by = 20


class entrada_edit(SuccessMessageMixin, UpdateView):
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
    
    return render(request, "entrada/entrada_cadastro.html", {'form': form})


def delete_cadastro(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)

    if request.method == "POST":
        entrada.delete()
        messages.warning(request, "Entrada excluída com sucesso")

    return redirect("entrada")