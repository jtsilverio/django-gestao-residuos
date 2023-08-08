from django.forms import ModelForm, TextInput
from apps.fornecedor.models import Fornecedor


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor

        fields = [
            "nome",
            "id_destinacao"
        ]

        labels = {
            "nome": "Nome",
            "id_destinacao": "Destinação"
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome da Classe",
                },
            ),
            # make id_destinacao a drodown
            "id_destinacao": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Destinação",
                },
            ),  
        }
