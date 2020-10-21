from django import forms
from .models import (contrato,
                     document,
                     imagem)



class contratoform(forms.ModelForm):
   # numcontrato = forms.CharField(
    #widget=forms.TextInput(attrs={'readonly':'readonly'})
#)
    class Meta:
        model = contrato
        fields = ['numcontrato', 'aluguel', 'imovel', 'morador','status','data_entrada', 'vigencia', 'vencimento']


class documentform(forms.ModelForm):
    class Meta:
        model = document
        fields = ['documento']


class photoform(forms.ModelForm):
    class Meta:
        model = imagem
        fields = ['foto']

