from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from imoveis.models import Imovel
from moradores.models import moradores
from contratos.models import contrato
from proprietario.models import proprietarios


def home(request):

    user = User.objects.filter(username='condado')
    if user:
        return render(request, 'home/home.html')

    else:
        ultimo_id = User.objects.create_user(username='nome do seu sistema', email='sistemacondado@gmail.com', password='sua senha').id

        proprietarios.objects.create(nome='master', identidade='111111111', cpf='22222222222', telefone='33333333333',
                                     endereco='endereco', numero='numero', bairro='bairro', cidade='cidade',
                                     cep=80010130, estado='estado', userid=ultimo_id)
        User.objects.filter(username='condado').update(is_superuser=1)
        return render(request, 'home/home.html')


@login_required()
def my_logout(request):
    logout(request)
    return redirect('home')


@login_required()
def homePageSistema(request):
    return render(request, 'home/sistema.html')


## implementação da tela de dashboard do sistema
@login_required()
def dashboardView(request):

    data = {}
    data['count_realState'] = Imovel.objects.filter(userid=request.user.id).count()
    data['count_morador'] = moradores.objects.filter(userid=request.user.id).count()
    data['count_contratos'] = contrato.objects.filter(userid=request.user.id).count()
    return render(request, 'home/sistema.html', data)




