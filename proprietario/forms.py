from django.forms import ModelForm
from .models import proprietarios

class formproprietario(ModelForm):
    class Meta:
        model = proprietarios
        # fields = ['nome', 'cpf', 'identidade', 'natural', 'estadocivil', 'profissao', 'telefone']
        fields = ['nome','identidade','cpf','username','password','password2','email','cep','telefone','endereco','numero',
                 'bairro','cidade','estado']

        #fields = ['nome','identidade','cpf','cep','telefone','endereco','numero',
        #'bairro', 'cidade', 'estado']

