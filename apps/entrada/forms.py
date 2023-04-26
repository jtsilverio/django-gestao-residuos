from django import forms
from apps.entrada.models import Entrada


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada

        fields = [
            "dt_entrada",
            "id_localidade",
            "id_classe",
            "peso",
        ]

        labels = {
            "dt_entrada": "Data de Entrada",
            "id_localidade": "Localidade",
            "id_classe": "Classe",
            "peso": "Peso",
        }

        widgets = {
            "dt_entrada": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "id_localidade": forms.Select(
                attrs={"class": "form-select", "placeholder": "Localidade"}
            ),
            "id_classe": forms.Select(
                attrs={"class": "form-select", "placeholder": "Classe"}
            ),
            "peso": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Localidade"},
            ),
        }
