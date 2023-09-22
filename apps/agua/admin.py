from django.contrib import admin

from apps.agua.models import Agua


class AguaAdmin(admin.ModelAdmin):
    list_display = [
        "id_agua",
        "id_localidade",
        "id_fornecedor",
        "dt_agua",
        "consumo",
        "custo",
    ]
    list_display_links = [
        "id_agua",
        "id_localidade",
        "id_fornecedor",
        "dt_agua",
        "consumo",
        "custo",
    ]
    list_filter = ["id_localidade", "id_fornecedor", "dt_agua"]
    search_fields = ["id_localidade", "id_fornecedor", "dt_agua"]
    list_per_page = 15


admin.site.register(Agua, AguaAdmin)
