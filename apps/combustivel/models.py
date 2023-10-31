from django.db import models

class Combustivel(models.Model):
    id_combustivel = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=250, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField()
    class Meta:
        db_table = "combustivel"
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'
        def __str__(self):
            return self.descricao
# Create your models here.
