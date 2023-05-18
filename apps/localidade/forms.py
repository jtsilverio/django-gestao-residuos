from django.forms import TextInput, ModelForm
from apps.localidade.models import Localidade


class LocalidadeForm(ModelForm):
    class Meta:
        model = Localidade

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
                    "placeholder": "Nome da Localidade",
                },
            )
        }
