from django.forms import ModelForm, TextInput

from apps.tipo_combustivel.models import TipoCombustivel


class TipoCombustivelForm(ModelForm):
    class Meta:
        model = TipoCombustivel

        fields = [
            "nome",
        ]

        labels = {
            "nome": "Tipo de Combustível",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tipo de Combustível",
                },
            )
        }
