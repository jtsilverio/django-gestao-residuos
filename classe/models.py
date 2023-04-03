from django.db import models

class Classe(models.Model):
    id_classe = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "classe"
        verbose_name = "Classe"
        verbose_name_plural = "Classes"