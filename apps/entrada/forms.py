from django.forms import DateInput, ModelChoiceField, ModelForm, NumberInput, Select

from apps.entrada.models import Entrada


class EntradaForm(ModelForm):
    class Meta:
        model = Entrada

        fields = [
            "data",
            "id_cluster",
            "id_classe",
            "peso",
        ]

        labels = {
            "data": "Data de Entrada",
            "id_cluster": "Cluster",
            "id_classe": "Classe",
            "peso": "Peso",
        }

        widgets = {
            "data": DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "id_cluster": Select(
                attrs={"class": "form-select", "placeholder": "Localidade"}
            ),
            "id_classe": Select(
                attrs={"class": "form-select", "placeholder": "Classe"}
            ),
            "peso": NumberInput(
                attrs={"class": "form-control", "placeholder": "Localidade"},
            ),
        }
