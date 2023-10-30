from django.contrib import admin

from apps.agua.models import Agua


class AguaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "id_localidade",
        "data",
        "consumo",
    ]
    list_display_links = [
        "id",
        "id_localidade",
        "data",
        "consumo",
    ]
    list_filter = ["id_localidade", "data"]
    search_fields = ["id_localidade", "data"]
    list_per_page = 15


admin.site.register(Agua, AguaAdmin)
