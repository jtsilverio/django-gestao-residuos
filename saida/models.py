from django.db import models
from classe.models import Classe
from localidade.models import Localidade
from fornecedor.models import Fornecedor
from fornecedor.models import Destinacao
from django.contrib import admin


# Create your models here.
class Saida(models.Model):
    id_saida = models.AutoField(primary_key=True)
    id_classe = models.ForeignKey(
        Classe, models.DO_NOTHING, db_column="id_classe"
    )
    id_localidade = models.ForeignKey(
        Localidade, models.DO_NOTHING, db_column="id_localidade"
    )
    id_fornecedor = models.ForeignKey(
        Fornecedor, models.DO_NOTHING, db_column="id_fornecedor"
    )
    id_destinacao = models.ForeignKey(
        Destinacao, models.DO_NOTHING, db_column="id_destinacao"
    )
    dt_saida = models.DateField(null=False, blank=False)
    peso = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=False
    )
    receita = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=True
    )
    custo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=True
    )
    mtr = models.CharField(max_length=50)
    cdf = models.CharField(max_length=50)

    def __str__(self):
        return f"ID:{self.id_saida}"

    class Meta:
        db_table = "saida"
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
