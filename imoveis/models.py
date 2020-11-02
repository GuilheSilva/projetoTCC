from django.db import models
from home.managers import dashboarsDados
from django.db.models import Count
import datetime


# insere o proximo id get do banco de dados e insere no proximo cadastro;
# -- verificar como desabilitar o imput do id para não ser alterado pelo usuarios, foi alterado a
# linha 20 id = models.IntegerField(primary_key=True, default= auto_id_morador, editable = False) mas consta erros......
#def auto_id_imoveis():

    #ultimo = Imovel.objects.all().order_by('id').last()
    #if not ultimo:
        #return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
    #ultimo_id = ultimo.id
    #ultimo_int = int(ultimo_id)
   # new_int = ultimo_int+1
    #new_id = str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2)+ '-' + str(new_int).zfill(2)
    #return new_int

# class Imovel que atribui os campos no banco
class Imovel(models.Model):

    STATUS_CHOICES = (
       ("Desocupado", "Desocupado"),
    )
    FINS_CHOICES = (
        ("Aluguel","Aluguel"),
    )

    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=False, null=False)
    fins = models.CharField(max_length=10, choices=FINS_CHOICES, blank=False, null=False)
    cep = models.CharField(max_length=30)
    endereco = models.CharField(max_length=60)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length= 30)
    estado = models.CharField(max_length=30)
    garagem = models.IntegerField()
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    userid = models.IntegerField()

    # mostra os dados no dashboarder em home/sistema.html
    objects = dashboarsDados()

    def __str__(self):
      return self.endereco + ', n°: ' + str(self.numero) + ', complemento: ' + self.complemento

