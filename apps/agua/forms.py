from django.forms import ModelChoiceField, ModelForm, Select, TextInput

from apps.agua.models import Agua
from apps.fornecedor.models import Fornecedor


class AguaForm(ModelForm):
    id_fornecedor = ModelChoiceField(
        label="Fornecedor",
        queryset=Fornecedor.objects.filter(tp_fornecedor__exact="Água"),
        widget=Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Agua

        fields = [
            "id_localidade",
            "id_fornecedor",
            "fonte_captacao",
            "dt_agua",
            "consumo",
            "custo",
        ]

        labels = {
            "id_localidade": "Localidade",
            "id_fornecedor": "Fornecedor",
            "fonte_captacao": "Fonte de Captação",
            "dt_agua": "Data",
            "consumo": "Consumo",
            "custo": "Custo",
        }

        widgets = {
            "id_localidade": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Localidade",
                }
            ),
            "id_fornecedor": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Fornecedor",
                }
            ),
            "fonte_captacao": TextInput(attrs={"class": "form-control"}),
            "dt_agua": TextInput(attrs={"class": "form-control"}),
            "consumo": TextInput(attrs={"class": "form-control"}),
            "custo": TextInput(attrs={"class": "form-control"}),
        }
