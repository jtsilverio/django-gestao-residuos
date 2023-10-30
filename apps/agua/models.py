from django.db import models

from apps.localidade.models import Localidade


class Agua(models.Model):
    FONTE_CHOICES = [
        ("Ligação Municipal", "Ligação Municipal"),
        ("Poço", "Poço"),
        ("Captação Superfície", "Captação Superfície"),
        ("Caminhão Pipa", "Caminhão Pipa"),
    ]

    id = models.AutoField(primary_key=True)
    id_localidade = models.ForeignKey(
        Localidade,
        models.DO_NOTHING,
        db_column="id_localidade",
    )
    data = models.DateField(null=False, blank=False)
    fonte = models.CharField(
        max_length=20,
        choices=FONTE_CHOICES,
        null=False,
        blank=False,
    )
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
        db_table = "agua"
        verbose_name = "Consumo de água"
        verbose_name_plural = "Consumo de água"
        ordering = ["-id"]
