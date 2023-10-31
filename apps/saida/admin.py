from django.contrib import admin

from .models import Saida


class SaidaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_classe",
        "id_cluster",
        "id_fornecedor",
        "id_destinacao",
        "data",
        "peso",
        "receita",
        "custo",
        "n_evidencia",
        "cdf",
    ]
    list_filter = [
        "id_classe",
        "id_cluster",
        "id_fornecedor",
        "id_destinacao",
        "data",
    ]
    search_fields = [
        "id_classe__nome",
        "id_cluster__nome",
        "id_fornecedor__nome",
        "id_destinacao__nome",
        "data",
    ]
    list_per_page = 15


admin.site.register(Saida, SaidaAdmin)
