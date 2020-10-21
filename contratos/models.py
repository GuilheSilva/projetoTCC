import datetime
from django.db import models
from moradores.models import moradores
from imoveis.models import Imovel
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save


"""def geracaoNumContrato(self):
    ultimoID = self.objects.all().order_by('numcontrato').last() #max
    if not ultimoID:
        return str(datetime.date.today().year) + '0'
    ultimo_ID = ultimoID.numcontrato
    ultimo = int(ultimo_ID)
    novo_contrato = ultimo + 1
    return novo_contrato"""

def geracaoNumContrato():
    ultimoID = contrato.objects.all().order_by('numcontrato').last() #max
    if not ultimoID:
        return str(datetime.date.today().year) + '0'
    ultimo_ID = ultimoID.numcontrato
    ultimo = int(ultimo_ID)
    novo_contrato = ultimo + 1
    return novo_contrato

class contrato(models.Model):
    """@staticmethod
    def get_next_number():
       # print('teste')
        teste = contrato.objects.count() + 1
        #print(teste)
        return teste"""

    ENCERRAMENTO_CHOICES = (
        ("Ativo", "Ativo"),

    )

    numcontrato = models.CharField(max_length=15,null=False)
    aluguel = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    imovel = models.ForeignKey(Imovel,verbose_name='Imoveis', blank=False, on_delete=models.PROTECT)
    #imovel = models.ForeignKey(Imovel,limit_choices_to= {'status': 'Desocupado'}, blank=False, on_delete=models.PROTECT)
    #imovel = models.ForeignKey(Imovel, limit_choices_to={'contrato__count__lt': 1}, blank=False, on_delete=models.PROTECT)
    #imovel = models.ForeignKey(Imovel, limit_choices_to= models.Q(status__in = ['Alugado']), blank=False, on_delete=models.PROTECT)
    morador = models.ForeignKey(moradores, null=True,blank=True,on_delete=models.PROTECT)
    status = models.CharField(max_length=15, null=False, choices=ENCERRAMENTO_CHOICES)
    data_entrada = models.DateField()
    vigencia = models.IntegerField(blank=False, null=False)
    vencimento = models.DateField()
    userid = models.IntegerField()

    def __str__(self):
      return self.numcontrato

class document(models.Model):
    data = models.DateField(default=datetime.datetime.today())
    documento = models.ImageField(upload_to='documentos', null=False, blank=False)
    #contrato = models.ForeignKey(contrato,  null=False,blank=False,on_delete=models.PROTECT)
    contrato = models.CharField(max_length=15,null=False)

    def __str__(self):
        return str(self.documento)

class imagem(models.Model):
    data = models.DateField(default=datetime.datetime.today())
    foto = models.ImageField(upload_to='imagens', null=False, blank=False)
    contrato = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.foto











