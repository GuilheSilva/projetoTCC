from django.db import models
from imoveis.models import Imovel


class Despesas(models.Model):


    STATUS_CHOICES = (
        ("Manutenção", "Manutenção"),
    )

    tipo = models.CharField(max_length=10, choices=STATUS_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    observacao = models.TextField()
    userid = models.IntegerField()
    imoveis = models.ForeignKey(Imovel, blank=False, on_delete=models.PROTECT)

    def _str_(self):
        return self.tipo
