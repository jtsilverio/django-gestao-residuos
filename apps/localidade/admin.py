from django.contrib import admin

from .models import Localidade


class LocalidadeAdmin(admin.ModelAdmin):
    list_display = ["id_localidade", "nome"]
    list_display_links = ["id_localidade", "nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]
    list_per_page = 15


admin.site.register(Localidade, LocalidadeAdmin)
