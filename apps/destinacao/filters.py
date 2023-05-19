import django_filters
from django.forms import (
    TextInput,
)


class DestinacaoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        label="Nome",
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Tipo de Destinação",
            }
        ),
    )
