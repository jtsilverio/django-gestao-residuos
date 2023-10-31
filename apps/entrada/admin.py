from django.contrib import admin

from apps.entrada.models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_classe",
        "id_cluster",
        "data",
        "peso",
    ]
    list_filter = ["id_classe", "id_cluster", "data"]
    search_fields = ["id_classe__nome", "id_cluster__nome", "data"]
    list_per_page = 15


admin.site.register(Entrada, EntradaAdmin)
