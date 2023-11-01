from django.db import models

from apps.cluster.models import Cluster


class Eletricidade(models.Model):
    id = models.AutoField(primary_key=True)
    id_cluster = models.ForeignKey(
        Cluster,
        models.DO_NOTHING,
        db_column="id_cluster",
    )
    data = models.DateField(null=False, blank=False)
    consumo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"ID:{self.id}"

    class Meta:
        db_table = "eletricidade"
        verbose_name = "Eletricidade"
        verbose_name_plural = "Eletricidades"
        ordering = ["-id"]
