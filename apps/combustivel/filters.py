import django_filters
from django.forms import Select

from apps.fornecedor.models import Fornecedor


class CombustivelFilter(django_filters.FilterSet):
    id_fornecedor = django_filters.ModelChoiceFilter(
        label="Fornecedor",
        queryset=Fornecedor.objects.filter(tp_fornecedor__exact="Combustível"),
        widget=Select(attrs={"class": "form-select"}),
    )
