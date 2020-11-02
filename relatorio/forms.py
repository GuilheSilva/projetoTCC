from django.forms import ModelForm
from django import forms
from contratos.models import contrato

class imoveisForm(ModelForm):
    class Meta:

        model = contrato
        fields = ['imovel']


GEEKS_CHOICES = (
("1", "Todos"),
("2", "Ativo"),
("3", "Encerrado"),

)

class GeeksForm(forms.Form):
    options = forms.ChoiceField(choices = GEEKS_CHOICES)
