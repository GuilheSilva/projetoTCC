from django.db import models
from home.managers import dashboarsDados

# class morador que atribui os campos no banco
class moradores(models.Model):

    ESTADOCIVIL_CHOICES = (
         ("Solteiro", "Solteiro"),
         ("Casado", "Casado"),
         ("Divorciado", "Divorciado"),
         ("Viuvo", "Viuvo"),
         ("União Estavel", "União Estavel"),
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    identidade = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    natural = models.CharField(max_length=30)
    estadocivil = models.CharField(max_length=15, choices=ESTADOCIVIL_CHOICES)
    profissao = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    userid = models.IntegerField()

    # mostra os dados no dashboarder em home/sistema.html
    objects = dashboarsDados()

    def __str__(self):
        return self.nome




