from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin

from apps.entrada.models import Entrada
from apps.entrada.forms import EntradaForm
from apps.entrada.filters import EntradaFilter


class EntradaIndex(FilterView):
    model = Entrada
    context_object_name = "entradas"
    template_name = "entrada/entrada.html"
    filterset_class = EntradaFilter
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter the queryset based on the request parameters
        if self.request.GET.get("field_peso"):
            queryset = queryset.filter(
                peso__gt=self.request.GET.get("field_peso")
            )
            queryset = queryset.filter(
                peso__lt=self.request.GET.get("field_peso")
            )

        return queryset


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
