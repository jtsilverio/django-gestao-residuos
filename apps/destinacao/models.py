from django.db import models

class Destinacao(models.Model):
    id_destinacao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "destinacao"
        ordering = ["nome"]
        verbose_name = "Destinação"
        verbose_name_plural = "Destinações"
