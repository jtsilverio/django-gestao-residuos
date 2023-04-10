from django.contrib import admin
from .models import Fornecedor, Destinacao

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["id_fornecedor", "nome"]
    list_display_links = ["id_fornecedor", "nome"]

class DestinacaoAdmin(admin.ModelAdmin):
    list_display = ["id_destinacao", "nome"]
    list_display_links = ["id_destinacao", "nome"]

admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Destinacao, DestinacaoAdmin)

