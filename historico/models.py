from django.db import models
from moradores.models import moradores
from imoveis.models import Imovel

class historico_contrato(models.Model):

    ENCERRAMENTO_CHOICES = (
        ("Ativo", "Ativo"),

    )

    numcontrato = models.CharField(max_length=15,null=False)
    aluguel = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    imovel = models.ForeignKey(Imovel,verbose_name='Imoveis', blank=False, on_delete=models.PROTECT)
    #imovel = models.ForeignKey(Imovel,limit_choices_to= {'status': 'Desocupado'}, blank=False, on_delete=models.PROTECT)
    #imovel = models.ForeignKey(Imovel, limit_choices_to={'contrato__count__lt': 1}, blank=False, on_delete=models.PROTECT)
    #imovel = models.ForeignKey(Imovel, limit_choices_to= models.Q(status__in = ['Alugado']), blank=False, on_delete=models.PROTECT)
    morador = models.CharField(max_length=40)
    status = models.CharField(max_length=15, null=False, choices=ENCERRAMENTO_CHOICES)
    data_entrada = models.DateField()
    vigencia = models.IntegerField(blank=False, null=False)
    vencimento = models.DateField()
    data_encerramento = models.DateField(blank=True, null=True)
    userid = models.IntegerField()

    def __str__(self):
      return self.numcontrato