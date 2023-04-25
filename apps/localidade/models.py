from django.db import models


# Create your models here.
class Localidade(models.Model):
    id_localidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.id_localidade}: {self.nome}"

    class Meta:
        db_table = "localidade"
        verbose_name = "Localidade"
        verbose_name_plural = "Localidades"
