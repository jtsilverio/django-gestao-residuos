from django.db import models

from apps.cluster.models import Cluster


# Create your models here.
class UnidadeConsumo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False, blank=False)
    id_cluster = models.ForeignKey(
        Cluster,
        models.DO_NOTHING,
        db_column="id_cluster",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "unidade_consumo"
        verbose_name = "Unidade de Consumo"
        verbose_name_plural = "Unidades de Consumo"
        ordering = ["-id"]
