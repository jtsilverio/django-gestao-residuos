from django.db import models

from apps.combustivel.models import Fornecedor
from apps.localidade.models import Localidade


class Agua(models.Model):
    id_agua = models.AutoField(primary_key=True)
    id_localidade = models.ForeignKey(
        Localidade,
        models.DO_NOTHING,
        db_column="id_localidade",
    )
    id_fornecedor = models.ForeignKey(
        Fornecedor,
        models.DO_NOTHING,
        db_column="id_fornecedor",
    )
    dt_agua = models.DateField(null=False, blank=False)
    consumo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
    )
    custo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"ID:{self.id_agua}"

    class Meta:
        db_table = "agua"
        verbose_name = "Consumo de água"
        verbose_name_plural = "Consumo de água"
        ordering = ["-id_agua"]
