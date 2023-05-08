import django_filters
from apps.saida.models import Saida
from apps.classe.models import Classe
from apps.localidade.models import Localidade
from apps.fornecedor.models import Fornecedor, Destinacao
from django.forms import DateInput, ModelChoiceField, BooleanField, ModelMultipleChoiceField, CheckboxSelectMultiple, SelectMultiple, Select, CheckboxInput, CharField

class SaidaFilter(django_filters.FilterSet):
    dt_saida = django_filters.DateFilter(label='Data de Saida', widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    id_fornecedor = django_filters.ModelChoiceFilter(label='Fornecedor', queryset=Fornecedor.objects.all(), widget=Select(attrs={'class': 'form-select'}))
    id_destinacao = django_filters.ModelChoiceFilter(label='Destinação', queryset=Destinacao.objects.all(), widget=Select(attrs={'class': 'form-select'}))
    id_classe = django_filters.ModelMultipleChoiceFilter(label='Classe', queryset=Classe.objects.all(), widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    id_localidade = django_filters.ModelMultipleChoiceFilter(label='Localidade', queryset=Localidade.objects.all(), widget=CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
