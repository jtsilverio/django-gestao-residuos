from django.forms import (
    CheckboxSelectMultiple,
    ChoiceField,
    ModelForm,
    ModelMultipleChoiceField,
    Select,
    TextInput,
)

from apps.destinacao.models import Destinacao
from apps.fornecedor.models import Fornecedor


class FornecedorForm(ModelForm):
    TP_FORNECEDOR_CHOICES = [
        (None, "Selecione..."),
        ("Resíduos", "Resíduos"),
        ("Água", "Água"),
        ("Eletricidade", "Eletricidade"),
        ("Combustível", "Combustível"),
    ]

    tp_fornecedor = ChoiceField(
        label="Tipo Fornecedor",
        choices=TP_FORNECEDOR_CHOICES,
        widget=Select(attrs={"class": "form-select"}),
    )

    destinacao = ModelMultipleChoiceField(
        label="Destinação",
        queryset=Destinacao.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input mb-0"}),
        required=False,
    )

    class Meta:
        model = Fornecedor

        fields = ["nome", "tp_fornecedor", "destinacao"]
        labels = {
            "nome": "Nome",
            "tp_fornecedor": "Tipo Fornecedor",
            "destinacao": "Destinação",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Fornecedor",
                },
            ),
        }
