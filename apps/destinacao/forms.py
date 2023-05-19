from django.forms import ModelForm, TextInput

from apps.destinacao.models import Destinacao


class DestinacaoForm(ModelForm):
    class Meta:
        model = Destinacao

        fields = [
            "nome",
        ]

        labels = {
            "nome": "Nome",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tipo de Destinação",
                },
            )
        }
