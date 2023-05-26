from django.contrib import admin

from apps.entrada.models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_classe",
        "id_localidade",
        "data",
        "peso",
    ]
    list_filter = ["id_classe", "id_localidade", "data"]
    search_fields = ["id_classe__nome", "id_localidade__nome", "data"]
    list_per_page = 15


admin.site.register(Entrada, EntradaAdmin)
