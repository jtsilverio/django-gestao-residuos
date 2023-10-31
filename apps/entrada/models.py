from django.db import models

from apps.classe.models import Classe
from apps.cluster.models import Cluster


class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    data = models.DateField(null=False, blank=False)
    id_classe = models.ForeignKey(
        Classe,
        models.DO_NOTHING,
        db_column="id_classe",
    )
    id_cluster = models.ForeignKey(
        Cluster,
        models.DO_NOTHING,
        db_column="id_cluster",
    )
    peso = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"ID:{self.id_entrada}"

    class Meta:
        db_table = "entrada"
        ordering = ["-id_entrada"]
