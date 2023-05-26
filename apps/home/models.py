from django.db import models


class EntradaMensal(models.Model):
    mes = models.CharField(max_length=50)
    ano = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    classe = models.CharField(max_length=50)
    localidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mes}: {self.peso}"

    class Meta:
        verbose_name_plural = "Entrada Mensal"
        managed = False
        db_table = 'v_entrada_mensal'


class SaidaMensal(models.Model):
    mes = models.CharField(max_length=50)
    ano = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    receita = models.DecimalField(max_digits=5, decimal_places=2)
    custo = models.DecimalField(max_digits=5, decimal_places=2)
    classe = models.CharField(max_length=50)
    localidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mes}: {self.peso}"

    class Meta:
        verbose_name_plural = "Saida Mensal"
        managed = False
        db_table = 'v_saida_mensal'