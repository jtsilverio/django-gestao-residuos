import django_filters
from django.forms import Select, TextInput
from django_filters import ModelChoiceFilter

from apps.cluster.models import Cluster


class UnidadeConsumoFilter(django_filters.FilterSet):
    # create a filter for a text field
    id_cluster = ModelChoiceFilter(
        queryset=Cluster.objects.all(),
        label="Cluster",
        widget=Select(
            attrs={
                "class": "form-select",
                "placeholder": "Cluster",
            }
        ),
    )

    nome = django_filters.CharFilter(
        label="Nome",
        lookup_expr="icontains",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Unidade de Consumo",
            }
        ),
    )
