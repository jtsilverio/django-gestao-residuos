from django.forms import ModelForm, TextInput

from apps.classe.models import Classe


class ClasseForm(ModelForm):
    class Meta:
        model = Classe

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
                    "placeholder": "Nome da Classe",
                },
            )
        }
