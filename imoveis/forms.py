from django.forms import ModelForm,CharField
from .models import Imovel


class ImoveisForm(ModelForm,):
    class Meta:

        model = Imovel
        fields = ['id','status','fins','cep','endereco','numero', 'complemento', 'bairro','cidade','estado', 'garagem',
                  'quartos','banheiros']
