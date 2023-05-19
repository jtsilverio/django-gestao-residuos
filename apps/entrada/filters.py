import django_filters
from django.forms import (BooleanField, CheckboxInput, CheckboxSelectMultiple,
                          DateInput, ModelChoiceField,
                          ModelMultipleChoiceField, Select, SelectMultiple)

from apps.classe.models import Classe
from apps.entrada.models import Entrada
from apps.localidade.models import Localidade


class EntradaFilter(django_filters.FilterSet):
    dt_entrada = django_filters.DateFilter(
        label="Data de Entrada",
        widget=DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    id_classe = django_filters.ModelMultipleChoiceFilter(
        label="Classe",
        queryset=Classe.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )
    id_localidade = django_filters.ModelMultipleChoiceFilter(
        label="Localidade",
        queryset=Localidade.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )
