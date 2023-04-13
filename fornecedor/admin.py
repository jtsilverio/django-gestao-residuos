from django.contrib import admin

from .models import Destinacao, Fornecedor


class FornecedorInline(admin.TabularInline):
    model = Fornecedor.id_destinacao.through
    extra = 0


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["id_fornecedor", "nome"]
    list_display_links = ["id_fornecedor", "nome"]


class DestinacaoAdmin(admin.ModelAdmin):
    list_display = ["id_destinacao", "nome"]
    list_display_links = ["id_destinacao", "nome"]
    inlines = [FornecedorInline]


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Destinacao, DestinacaoAdmin)
