from django.db import models

# class morador que atribui os campos no banco
class proprietarios(models.Model):

    # ESTADOCIVIL_CHOICES = (
    #     ("Solteiro", "Solteiro"),
    #     ("Casado", "Casado"),
    #     ("Divorciado", "Divorciado"),
    #     ("Viuvo", "Viuvo"),
    #     ("União Estavel", "União Estavel"),
    # )
    nome = models.CharField(max_length=50)
    identidade = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    cep = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    userid = models.IntegerField()

    # username = models.CharField(max_length=30)
    # password = models.CharField(max_length=30)
    # password2 = models.CharField(max_length=30)
    # email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

