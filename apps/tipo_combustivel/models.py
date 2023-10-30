from django.db import models


# Create your models here.
class TipoCombustivel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "tp_combustivel"
        verbose_name = "Tipo de Combustível"
        verbose_name_plural = "Tipos de Combustíveis"
        ordering = ["-id"]
