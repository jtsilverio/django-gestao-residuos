import django_filters
from django.forms import Select


class AguaFilter(django_filters.FilterSet):
    # create a filter for a text field
    nome = django_filters.CharFilter(
        label="Nome",
        lookup_expr="iexact",
        widget=Select(attrs={"class": "form-select"}),
    )
