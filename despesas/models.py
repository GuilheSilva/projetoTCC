from django.db import models
from imoveis.models import Imovel


class Despesas(models.Model):


    STATUS_CHOICES = (
        ("Manutenção", "Manutenção"),
        ("Água", "Água"),
        ("Eletricidade", "Eletricidade"),
        ("Imposto", "Imposto"),
        ("Outro", "Outro"),
    )

    tipo = models.CharField(max_length=25, choices=STATUS_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    observacao = models.TextField()
    nota_fiscal = models.IntegerField(null=True)
    userid = models.IntegerField()
    imoveis = models.ForeignKey(Imovel, blank=False, on_delete=models.PROTECT)

    def _str_(self):
        return self.tipo
