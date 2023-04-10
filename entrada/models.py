from django.db import models
from classe.models import Classe
from localidade.models import Localidade

class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    id_classe = models.ForeignKey(Classe, models.DO_NOTHING, db_column="id_classe")
    id_localidade = models.ForeignKey(Localidade, models.DO_NOTHING, db_column="id_localidade")
    dt_entrada = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
            return f"ID:{self.id_entrada}"
    
    class Meta:
        db_table = "entrada"