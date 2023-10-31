from django.forms import ModelForm, Select, TextInput

from apps.unidade_consumo.models import UnidadeConsumo


class UnidadeConsumoForm(ModelForm):
    class Meta:
        model = UnidadeConsumo

        fields = [
            "nome",
            "id_cluster",
        ]

        labels = {
            "nome": "Unidade de Consumo",
            "id_cluster": "Cluster",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Unidade de Consumo",
                },
            ),
            "id_cluster": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Cluster",
                },
            ),
        }
