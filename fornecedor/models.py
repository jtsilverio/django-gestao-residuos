from django.db import models

class Destinacao(models.Model):
    id_destinacao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f"{self.id_destinacao}: {self.nome}"
    
    class Meta:
        db_table = "destinacao"
        ordering = ["nome"]
        verbose_name = "Destinação"
        verbose_name_plural = "Destinações"
    
    
class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    id_destinacao = models.ManyToManyField(Destinacao, db_table="fornecedor_destinacao", related_name="destinacao")
    
    def __str__(self):
        return f"{self.id_fornecedor}: {self.nome}"
    
    class Meta:
        db_table = "fornecedor"
        ordering = ["nome"]
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


