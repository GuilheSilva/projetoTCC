from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from imoveis.models import Imovel
from moradores.models import moradores
from contratos.models import contrato
from proprietario.models import proprietarios
from historico.models import historico_contrato
from datetime import datetime
from despesas.models import Despesas
import json


def home(request):
    user = User.objects.filter(username='condado')
    if user:
        return render(request, 'home/home.html')

    else:
        ultimo_id = User.objects.create_user(username='condado', email='sistemacondado@gmail.com',
                                             password='chaves2508').id

        proprietarios.objects.create(nome='master', identidade='111111111', cpf='22222222222', telefone='33333333333',
                                     endereco='endereco', numero='numero', bairro='bairro', cidade='cidade',
                                     cep=80010130, estado='estado', userid=ultimo_id)
        User.objects.filter(username='condado').update(is_superuser=1)
        return render(request, 'home/charts.html')


@login_required()
def my_logout(request):
    logout(request)
    return redirect('home')


@login_required()
def homePageSistema(request):
    # labels = ['Ativos','Encerrados]
    # data = []
    # contratos ativos para o pie charts
    # contrato.objects.filter(userid=request.user.id, status='Ativo').count() 
    # contratos Encerrados apra o pie charts
    # contrato.objects.filter(userid=request.user.id, status='Encerrados').count() 

    return render(request, 'home/sistema.html')


## implementação da tela de dashboard do sistema
@login_required()
def dashboardView(request):
    # data['somaContratos'] = soma_valores_contrato(request)[0]
    # data['somaContratosReceber'] = soma_valores_contrato(request)[1]
    # data['despesas'] = soma_despesas(request)
    # data['historico'] = calulca_historico(request)

    # charts pie 'pizza' despesas quantidade
    manutencao = Despesas.objects.filter(userid=request.user.id, tipo='Manutencao').count()
    agua = Despesas.objects.filter(userid=request.user.id, tipo='Água').count()
    eletricidade = Despesas.objects.filter(userid=request.user.id, tipo='Eletricidade').count()
    imposto = Despesas.objects.filter(userid=request.user.id, tipo='Imposto').count()
    outros = Despesas.objects.filter(userid=request.user.id, tipo='Outro').count()

    # charts  pie 'pizza' contratos quantidade
    encerrado = contrato.objects.filter(userid=request.user.id, status='Encerrado').count()
    ativos = contrato.objects.filter(userid=request.user.id, status='Ativo').count()

    context = {
        # contratos
        'ativos': json.dumps(ativos),
        'encerrados': json.dumps(encerrado),
        # despesas
        'manutencao': json.dumps(manutencao),
        'agua': json.dumps(agua),
        'eletricidade': json.dumps(eletricidade),
        'imposto': json.dumps(imposto),
        'outros': json.dumps(outros),
        # dashboard
        'count_realState': Imovel.objects.filter(userid=request.user.id).count(),
        'count_morador': moradores.objects.filter(userid=request.user.id).count(),
        'count_contratos': contrato.objects.filter(userid=request.user.id).count(),
        'count_despesas': Despesas.objects.filter(userid=request.user.id).count()
    }
    # print(context['names'],context['prices'])
    return render(request, 'home/sistema.html', context)


# def charts(request):
#     encerrado = contrato.objects.filter(userid=request.user.id, status='Encerrado').count()
#     ativos = contrato.objects.filter(userid=request.user.id, status='Ativo').count()
#     # data1 = {
#     #     'data1': [
#     #         {
#     #             'encerrados': encerrado,
#     #             'ativos': ativos,
#     #         }
#     #
#     #     ]
#     # }
#     # return JsonResponse(data1)
#
#     return render(request, 'home/sistema.html', context)


def soma_valores_contrato(request):
    data_atual = datetime.today()
    print(data_atual)
    contratos = contrato.objects.filter(userid=request.user.id, status='Ativo')
    recebe_data = str(data_atual)
    pega_data = recebe_data[0:10]
    d1 = datetime.strptime(pega_data, "%Y-%m-%d")
    print(d1)
    somaContratos = 0
    for i in contratos:
        if d1.date() > i.data_entrada:
            dias = abs((d1.date() - i.data_entrada).days)
            print(dias)
            calcula_dias = dias / 30
            arredonda_dias = round(calcula_dias, 1)
            intervaloMeses = int(arredonda_dias)
            somaContratos = somaContratos + (float(i.aluguel) * intervaloMeses)
    somaContratosReceber = 0
    for j in contratos:
        if d1.date() > j.data_entrada:
            dias = abs((d1.date() - j.vencimento).days)
            print(dias)
            calcula_dias = dias / 30
            arredonda_dias = round(calcula_dias, 1)
            intervaloMeses = int(arredonda_dias)
            somaContratosReceber = somaContratosReceber + (float(j.aluguel) * intervaloMeses)

    return somaContratos, somaContratosReceber


def soma_despesas(request):
    despesas = Despesas.objects.filter(userid=request.user.id)

    somaDespesas = 0

    for i in despesas:
        somaDespesas = somaDespesas + i.valor

    return somaDespesas


def calulca_historico(request):
    historico = historico_contrato.objects.filter(userid=request.user.id)

    somaHistorico = 0

    for j in historico:
        recebe_data_encerramento = str(j.data_encerramento)
        pega_data_1 = recebe_data_encerramento[0:10]
        data_de_encerramento = datetime.strptime(pega_data_1, "%Y-%m-%d")
        recebe_data_inicial = str(j.data_entrada)
        pega_data_2 = recebe_data_inicial[0:10]
        data_de_inicial = datetime.strptime(pega_data_2, "%Y-%m-%d")
        resultado_dias_historico = abs((data_de_encerramento.date() - data_de_inicial.date()).days)
        calcula_dias_historico = resultado_dias_historico / 30
        arredonda_dias_historico = round(calcula_dias_historico, 1)
        intervaloMeses_historico = int(calcula_dias_historico)
        somaHistorico = somaHistorico + (float(j.aluguel) * intervaloMeses_historico)

    return somaHistorico

# essa função serve para verificar o usuario master para ter acesso a configurações
# do sistema como o acesso ao banco, ip entre outros
def configLogin(request):
    # tem que criar o form ou usar um que já tenha feito
    # form = loginConfig(request.POST or None)
    # if form.isvalid():
        # username = form.cleaned_data.get('username')
        # senha = form.cleaned_data.get('username')
        #user = authenticate(username=username, password=senha, is_superuser=1)
        #return ('paginaConfig.html')
    return render(request, 'home/config.html')
