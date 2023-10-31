from django.db import models

from apps.classe.models import Classe
from apps.cluster.models import Cluster
from apps.fornecedor.models import Destinacao, Fornecedor


# Create your models here.
class Saida(models.Model):
    id_saida = models.AutoField(primary_key=True)
    id_classe = models.ForeignKey(Classe, models.DO_NOTHING, db_column="id_classe")
    id_cluster = models.ForeignKey(Cluster, models.DO_NOTHING, db_column="id_cluster")
    id_fornecedor = models.ForeignKey(
        Fornecedor, models.DO_NOTHING, db_column="id_fornecedor"
    )
    id_destinacao = models.ForeignKey(
        Destinacao, models.DO_NOTHING, db_column="id_destinacao"
    )
    data = models.DateField(null=False, blank=False)
    peso = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=False
    )
    receita = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=True
    )
    custo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=True
    )
    n_evidencia = models.CharField(max_length=50)
    cdf = models.CharField(
        max_length=50,
        blank=True,
        default="",
    )

    def __str__(self):
        return f"ID:{self.id_saida}"

    class Meta:
        db_table = "saida"
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
        ordering = ["-id_saida"]
