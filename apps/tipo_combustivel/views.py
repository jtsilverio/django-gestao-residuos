from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.tipo_combustivel.filters import TipoCombustivelFilter as ModelFilter
from apps.tipo_combustivel.forms import TipoCombustivelForm as ModelForm
from apps.tipo_combustivel.models import TipoCombustivel as Model
from apps.utils import (
    create_filtered_context,
    paginate_query,
)

APP_NAME = "tipo_combustivel"
APP_TITLE = "Tipo Combustível"


def index(request):
    model_filter = ModelFilter(request.GET, queryset=Model.objects.all())

    query_filtered = paginate_query(request, model_filter.qs, settings.PAGESIZE)
    context = create_filtered_context(query_filtered, model_filter, request)
    context["title"] = APP_TITLE
    context["app_name"] = APP_NAME

    return render(request, f"{APP_NAME}/index.html", context)


class Create(SuccessMessageMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = f"{APP_NAME}/create.html"
    success_message = f"{APP_TITLE} Cadastrado"
    extra_context = {"title": APP_TITLE, "app_name": APP_NAME}
    success_url = reverse_lazy(f"{APP_NAME}:index")


class Edit(SuccessMessageMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = f"{APP_NAME}/edit.html"
    success_message = f"{APP_TITLE} Atualizado"
    extra_context = {"title": APP_TITLE, "app_name": APP_NAME}
    success_url = reverse_lazy(f"{APP_NAME}:index")


def delete(request, pk):
    entry = get_object_or_404(Model, pk=pk)

    if request.method == "POST":
        entry.delete()
        messages.warning(request, f"{APP_TITLE} Excluído")

    return redirect(f"{APP_NAME}:index")
