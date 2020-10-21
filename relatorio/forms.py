from django.forms import ModelForm
from contratos.models import contrato

class imoveisForm(ModelForm):
    class Meta:

        model = contrato
        fields = ['imovel']
