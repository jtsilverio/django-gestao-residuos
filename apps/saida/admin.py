from django.contrib import admin
from .models import Saida


class SaidaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_classe",
        "id_localidade",
        "id_fornecedor",
        "id_destinacao",
        "dt_saida",
        "peso",
        "receita",
        "custo",
        "n_evidencia",
        "cdf",
    ]
    list_filter = [
        "id_classe",
        "id_localidade",
        "id_fornecedor",
        "id_destinacao",
        "dt_saida",
    ]
    search_fields = [
        "id_classe__nome",
        "id_localidade__nome",
        "id_fornecedor__nome",
        "id_destinacao__nome",
        "dt_saida",
    ]
    list_per_page = 15


admin.site.register(Saida, SaidaAdmin)
