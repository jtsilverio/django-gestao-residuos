from django.forms import (
    DateInput,
    ModelChoiceField,
    ModelForm,
    NumberInput,
    Select,
    SelectDateWidget,
    TextInput,
)

from apps.combustivel.models import Combustivel


class CombustivelForm(ModelForm):
    class Meta:
        model = Combustivel
        fields = [
            "dt_combustivel",
            "id_localidade",
            "fonte",
            "id_tp_combustivel",
            "consumo",
        ]
        labels = {
            "id_localidade": "Localidade",
            "id_tp_combustivel": "Tipo Combustível",
            "dt_combustivel": "Data",
            "fonte": "Fonte",
            "consumo": "Consumo (L)",
        }
        widgets = {
            "id_localidade": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Localidade",
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
