from django.conf import settings
from django.db import models


# Create your models here.
class Cluster(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25, blank=False, null=False)
    estado = models.CharField(
        max_length=2,
        blank=False,
        null=False,
        choices=settings.ESTADOS_BRASILEIROS,
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "cluster"
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"
        ordering = ["estado", "nome"]
