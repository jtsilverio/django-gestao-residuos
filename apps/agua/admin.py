from django.contrib import admin

from apps.agua.models import Agua


class AguaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "id_cluster",
        "data",
        "consumo",
    ]
    list_display_links = [
        "id",
        "id_cluster",
        "data",
        "consumo",
    ]
    list_filter = ["id_cluster", "data"]
    search_fields = ["id_cluster", "data"]
    list_per_page = 15


admin.site.register(Agua, AguaAdmin)
