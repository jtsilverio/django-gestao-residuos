from django.db import models

from apps.fornecedor.models import Fornecedor
from apps.localidade.models import Localidade


class Eletricidade(models.Model):
    id_eletricidade = models.AutoField(primary_key=True)
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
    dt_eletricidade = models.DateField(null=False, blank=False)
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
        return f"ID:{self.id_eletricidade}"

    class Meta:
        db_table = "eletricidade"
        verbose_name = "Eletricidade"
        verbose_name_plural = "Eletricidades"
        ordering = ["-id_eletricidade"]
