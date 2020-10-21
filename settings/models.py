from django.db import models

class importImoveis(models.Model):
    #filename = models.ImageField(upload_to='arquivos', null=False, blank=False)
    filename = models.FileField(upload_to='media')

    def __str__(self):
      return self.filename
