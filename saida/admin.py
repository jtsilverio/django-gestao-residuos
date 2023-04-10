from django.contrib import admin
from .models import Saida

class SaidaAdmin(admin.ModelAdmin):
    #fields = ['id_classe', 'id_localidade', 'id_fornecedor', 'id_destinacao', 'dt_saida', 'peso', 'receita', 'custo', 'mtr', 'cdf']
    list_display = ['id_saida', 'id_classe', 'id_localidade', 'id_fornecedor', 'id_destinacao', 'dt_saida', 'peso', 'receita', 'custo', 'mtr', 'cdf']
    #list_filter = ['id_classe', 'id_localidade', 'id_fornecedor', 'id_destinacao', 'dt_saida']
    #search_fields = ['id_classe', 'id_localidade', 'id_fornecedor', 'id_destinacao', 'dt_saida']
    #list_per_page = 10
    

admin.site.register(Saida, SaidaAdmin)
