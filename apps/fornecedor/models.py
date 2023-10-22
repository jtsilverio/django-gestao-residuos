from django.db import models

from apps.destinacao.models import Destinacao


class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    tp_fornecedor = models.CharField(max_length=50, null=False, blank=False)
    destinacao = models.ManyToManyField(
        Destinacao,
        db_table="fornecedor_destinacao",
        related_name="fornecedor",
        blank=True,
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "fornecedor"
        ordering = ["nome"]
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
