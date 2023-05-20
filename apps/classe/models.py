from django.db import models


class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "classe"
        verbose_name = "Classe"
        verbose_name_plural = "Classes"
        ordering = ["-id_classe"]