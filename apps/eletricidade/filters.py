from django.forms import DateInput, Select
from django_filters import ChoiceFilter, DateFilter, FilterSet, ModelChoiceFilter

from apps.cluster.models import Cluster
from apps.eletricidade.models import Eletricidade


class EletricidadeFilter(FilterSet):
    data = DateFilter(
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
        label="Cluster",
        queryset=Cluster.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
    )
