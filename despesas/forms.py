from despesas.models import Despesas
from django.forms import ModelForm, DateInput
from django import forms


class despesasForm(ModelForm):
    nota_fiscal = forms.IntegerField(required=False)
    class Meta:

        model = Despesas
        fields = ['tipo','valor', 'data', 'nota_fiscal', 'observacao','imoveis']
        widgets = {
            'data': DateInput(attrs={'class':'form-control', 'type':'date', 'max':'2100-12-31'})
        }




