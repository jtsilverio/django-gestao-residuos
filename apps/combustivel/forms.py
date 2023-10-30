from django.forms import (
    ModelChoiceField,
    ModelForm,
    Select,
    SelectDateWidget,
    TextInput,
)

from apps.combustivel.models import Combustivel
from apps.fornecedor.models import Fornecedor


class CombustivelForm(ModelForm):
    id_fornecedor = ModelChoiceField(
        label="Fornecedor",
        queryset=Fornecedor.objects.filter(tp_fornecedor__exact="Combustível"),
        widget=Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Combustivel
        fields = [
            "dt_combustivel",
            "id_fornecedor",
            "tp_combustivel",
            "consumo",
            "custo",
        ]
        labels = {
            "dt_combustivel": "Data",
            "id_fornecedor": "Fornecedor",
            "tp_combustivel": "Tipo de Combustível",
            "consumo": "Consumo",
            "custo": "Custo",
        }
