from django.shortcuts import render
from django.views.generic.detail import DetailView
from contratos.forms import contratoform
from contratos.models import  contrato


def historicoview(request):
    historico = contrato.objects.filter(userid=request.user.id, status='Encerrado')
    qtd = contrato.objects.filter(userid=request.user.id,status='Encerrado').count()
    return render(request, 'historico.html', context={'historico': historico, 'qtd': qtd})




# Create your views here.
