from django.contrib import admin
from apps.classe.models import Classe


class ClasseAdmin(admin.ModelAdmin):
    list_display = ["id_classe", "nome"]
    list_display_links = ["id_classe", "nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]
    list_per_page = 15


admin.site.register(Classe, ClasseAdmin)
