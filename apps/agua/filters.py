from django.forms import DateInput, Select
from django_filters import ChoiceFilter, DateFilter, FilterSet, ModelChoiceFilter

from apps.agua.models import Agua
from apps.localidade.models import Localidade


class AguaFilter(FilterSet):
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

    id_localidade = ModelChoiceFilter(
        label="Localidade",
        queryset=Localidade.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
    )

    fonte = ChoiceFilter(
        label="Fonte",
        choices=Agua.FONTE_CHOICES,
        widget=Select(attrs={"class": "form-select"}),
    )
