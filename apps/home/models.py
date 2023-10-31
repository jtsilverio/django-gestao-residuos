from django.db import models


class ResumoMensalResiduos(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=10)
    ano = models.CharField(max_length=5)
    mes = models.CharField(max_length=5)
    cluster = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    peso = models.FloatField()
    receita = models.FloatField()
    custo = models.FloatField()

    def __str__(self):
        return f"Resumo Mensal[Ano:{self.ano}; Mês:{self.mes}]"

    class Meta:
        verbose_name_plural = "Resumo Mensal Resíduos"
        managed = False
        db_table = "resumo_mensal_residuos"
