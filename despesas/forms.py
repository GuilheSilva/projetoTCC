from despesas.models import Despesas
from django.forms import ModelForm, DateInput


class despesasForm(ModelForm):
    class Meta:

        model = Despesas
        fields = ['tipo','valor', 'data', 'observacao','imoveis']
        widgets = {
            'data': DateInput(attrs={'class':'form-control', 'type':'date'})
        }




