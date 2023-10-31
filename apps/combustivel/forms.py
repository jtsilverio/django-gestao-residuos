from django.forms import (
    DateInput,
    ModelForm,
    NumberInput,
    Select,
)

from apps.combustivel.models import Combustivel


class CombustivelForm(ModelForm):
    class Meta:
        model = Combustivel
        fields = [
            "dt_combustivel",
            "id_cluster",
            "fonte",
            "id_tp_combustivel",
            "consumo",
        ]
        labels = {
            "id_cluster": "Cluster",
            "id_tp_combustivel": "Tipo Combustível",
            "dt_combustivel": "Data",
            "fonte": "Fonte",
            "consumo": "Consumo (L)",
        }
        widgets = {
            "id_cluster": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Cluster",
                }
            ),
            "id_tp_combustivel": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Tipo Combustível",
                }
            ),
            "dt_combustivel": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Data",
                    "type": "date",
                }
            ),
            "fonte": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Fonte",
                }
            ),
            "consumo": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Consumo",
                }
            ),
        }
