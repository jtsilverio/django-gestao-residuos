from django.forms import ModelForm, Select, TextInput

from apps.cluster.models import Cluster


class ClusterForm(ModelForm):
    class Meta:
        model = Cluster

        fields = [
            "nome",
            "estado",
        ]

        labels = {
            "nome": "Nome",
            "estado": "Estado",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Cluster",
                },
            ),
            "estado": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Estado",
                },
            ),
        }
