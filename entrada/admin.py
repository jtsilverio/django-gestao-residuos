from django.contrib import admin
from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_classe",
        "id_localidade",
        "dt_entrada",
        "peso",
    ]
    list_filter = ["id_classe", "id_localidade", "dt_entrada"]
    search_fields = ["id_classe__nome", "id_localidade__nome", "dt_entrada"]
    list_per_page = 15


admin.site.register(Entrada, EntradaAdmin)
