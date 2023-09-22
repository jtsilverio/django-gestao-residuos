from django.contrib import admin


class EletricidadeAdmin(admin.ModelAdmin):
    list_display = [
        "id_eletricidade",
        "id_localidade",
        "id_fornecedor",
        "dt_eletricidade",
        "consumo",
        "custo",
    ]
    list_display_links = [
        "id_eletricidade",
        "id_localidade",
        "id_fornecedor",
        "dt_eletricidade",
        "consumo",
        "custo",
    ]
    list_filter = ["id_localidade", "id_fornecedor", "dt_eletricidade"]
    search_fields = ["id_localidade", "id_fornecedor", "dt_eletricidade"]
    list_per_page = 15
