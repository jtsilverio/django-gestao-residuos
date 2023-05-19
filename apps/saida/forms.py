from django import forms

from apps.saida.models import Saida


class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida

        fields = [
            "dt_saida",
            "id_localidade",
            "id_classe",
            "peso",
            "id_fornecedor",
            "id_destinacao",
            "receita",
            "custo",
            "n_evidencia",
            "cdf",
        ]

        labels = {
            "dt_saida": "Data de Saída",
            "id_localidade": "Localidade",
            "id_classe": "Classe",
            "peso": "Peso",
            "id_fornecedor": "Fornecedor",
            "id_destinacao": "Destinação",
            "receita": "Receita",
            "custo": "Custo",
            "n_evidencia": "Nº Evidência",
            "cdf": "CDF",
        }

        widgets = {
            "dt_saida": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
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
            "id_fornecedor": forms.Select(
                attrs={"class": "form-select", "placeholder": "Fornecedor"}
            ),
            "id_destinacao": forms.Select(
                attrs={"class": "form-select", "placeholder": "Destinação"}
            ),
            "receita": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Receita"},
            ),
            "custo": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Custo"},
            ),
            "n_evidencia": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nº Evidência"},
            ),
            "cdf": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "CDF"},
            ),
        }
