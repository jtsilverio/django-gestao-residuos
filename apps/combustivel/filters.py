from django.forms import DateInput, Select
from django_filters import ChoiceFilter, DateFilter, FilterSet, ModelChoiceFilter

from apps.cluster.models import Cluster
from apps.combustivel.models import Combustivel


class CombustivelFilter(FilterSet):
    dt_combustivel = DateFilter(
        label="Data de Cadastro",
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "style": "max-width: 200px;",
            }
        ),
    )

    id_cluster = ModelChoiceFilter(
        label="Localidade",
        queryset=Cluster.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
    )

    fonte = ChoiceFilter(
        label="Fonte",
        choices=Combustivel.FONTE_CHOICES,
        widget=Select(attrs={"class": "form-select"}),
    )

    id_tp_combustivel = ModelChoiceFilter(
        label="Tipo de Combustível",
        queryset=Combustivel.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
    )
