from django.contrib import admin


class CombustivelAdmin(admin.ModelAdmin):
    list_display = [
        "id_combustivel",
        "id_cluster",
        "id_fornecedor",
        "dt_combustivel",
        "consumo",
        "custo",
    ]
    list_display_links = [
        "id_combustivel",
        "id_cluster",
        "id_fornecedor",
        "dt_combustivel",
        "consumo",
        "custo",
    ]
    list_filter = ["id_cluster", "id_fornecedor", "dt_combustivel"]
    search_fields = ["id_cluster", "id_fornecedor", "dt_combustivel"]
    list_per_page = 15
