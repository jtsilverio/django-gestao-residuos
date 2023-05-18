import django_filters
from django.forms import (
    TextInput,
)


class ClasseFilter(django_filters.FilterSet):
    # create a filter for a text field
    nome = django_filters.CharFilter(
        label="Nome",
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome da Classe",
            }
        ),
    )
