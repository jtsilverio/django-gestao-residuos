from django.db import models

from apps.cluster.models import Cluster
from apps.tipo_combustivel.models import TipoCombustivel


class Combustivel(models.Model):
    FONTE_CHOICES = [
        ("Fixa", "Fonte Fixa"),
        ("Móvel", "Fonte Móvel"),
    ]

    id = models.AutoField(primary_key=True)
    id_cluster = models.ForeignKey(
        Cluster,
        models.DO_NOTHING,
        db_column="id_cluster",
    )
    id_tp_combustivel = models.ForeignKey(
        TipoCombustivel,
        models.DO_NOTHING,
        db_column="id_tp_combustivel",
    )
    dt_combustivel = models.DateField(
        null=False,
        blank=False,
    )
    fonte = models.CharField(
        max_length=5,
        choices=FONTE_CHOICES,
        null=False,
        blank=False,
    )
    consumo = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"ID:{self.id}"

    class Meta:
        db_table = "combustivel"
        verbose_name = "Combustível"
        verbose_name_plural = "Combustíveis"
        ordering = ["-id"]
