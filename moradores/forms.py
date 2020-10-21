from django.forms import ModelForm
from .models import moradores

class moradorForm(ModelForm):
    class Meta:
        model = moradores
        fields = ['id', 'nome', 'identidade','cpf','natural','estadocivil','profissao', 'email', 'telefone']

