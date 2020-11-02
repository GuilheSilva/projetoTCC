from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views.generic.detail import DetailView
from xhtml2pdf import pisa
import io
from imoveis.models import Imovel
from moradores.models import moradores
from proprietario.models import proprietarios
from .models import historico_contrato
from contratos.models import contrato
from contratos.views import number_to_long_number
from contratos.models import document, imagem

@login_required()
def historicoview(request):
    historico = historico_contrato.objects.filter(userid=request.user.id, status='Encerrado')
    print('batata', historico)
    qtd = historico_contrato.objects.filter(userid=request.user.id, status='Encerrado').count()
    return render(request, 'historico.html', context={'historico': historico, 'qtd': qtd})


@login_required()
def historicoDetail(request, id):
    doclist = document.objects.filter(contrato=id)
    pholist = imagem.objects.filter(contrato=id)
    historico = get_object_or_404(historico_contrato, numcontrato=id)
    return render(request, 'historicoDetail.html', context={'historico': historico,
                                                            'doclist': doclist,
                                                            'pholist': pholist})


@login_required()
def doc_list(request, id):
    doclist = document.objects.filter(contrato=id)
    return render(request, 'documentoView.html', {'doclist': doclist})


# nessa função faz a listagem das fotos anexados no contrato.
@login_required()
def photo_view(request, id):
    pholist = imagem.objects.filter(contrato=id)
    return render(request, 'photo_view.html', {'pholist': pholist})


# Nessa Class ele converte o html em pdf
class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


# nessa função ele gera os dados que vai sair dentro dentro do PDF.
@login_required()
def quebra_contrato(request, id):
    # pega a data atual no formato de ano, mes e dia.
    # d = datetime.today().strftime('%y-%m-%d')

    # dados do proprietario
    proprietario = get_object_or_404(proprietarios, userid=request.user.id)
    # variavel do nome da geração do quebra cntrato
    quebra_contrato = 'encerramento'
    # busca os dados do contrato pelo numero do contrato
    dadoscontrato = get_object_or_404(historico_contrato, numcontrato=id)
    #variavel

    # busca os dados do imovel que foi selecionado no contrato.
    dadosimoveis = get_object_or_404(Imovel, id=dadoscontrato.imovel_id)
    # print(dadosimoveis)
    # busca os dados do morador que foi selecionado no contrato
    dadosmorador = get_object_or_404(moradores, nome=dadoscontrato.morador)
    # chama a função number_to_long_number e passa o valor do aluguel para extenso como string.
    aluguel_por_extenso = number_to_long_number(str(dadoscontrato.aluguel))
   # variavel
    contrat = dadoscontrato

    data = datetime.today().strftime('%d-%m-%y')
    dia = datetime.today().day
    ano = datetime.today().year
    data_atual = dataExtenso(data)

    # parametros de variaveis para inserir no layout do contrato
    params = {

        'nomeProprietario': proprietario.nome,
        'identidadeProprietario': proprietario.identidade,
        'cpfProprietario': proprietario.cpf,
        'cidadeProprietario': proprietario.cidade,
        'Numcontrato': dadoscontrato.numcontrato,
        'Morador': dadoscontrato.morador,
        'cpfMorador': dadosmorador.cpf,
        'identidadeMorador': dadosmorador.identidade,
        'naturaldeMorador': dadosmorador.natural,
        'estadocivilMorador': dadosmorador.estadocivil,
        'profissaoMorador': dadosmorador.profissao,
        'cependereco': dadosimoveis.cep,
        'Imovel': dadoscontrato.imovel,
        'numeroEndereco': dadosimoveis.numero,
        'bairroEndereco': dadosimoveis.bairro,
        'cidadeEndereco': dadosimoveis.cidade,
        'estadoEndereco': dadosimoveis.estado,
        'Entrada': dadoscontrato.data_entrada,
        'vigencia': dadoscontrato.vigencia,
        'Vencimento': dadoscontrato.vencimento,
        'Aluguel': dadoscontrato.aluguel,
        'Aluguel_extenso': aluguel_por_extenso,
        'diaAtual': dia,
        'mesAtualExtenso': data_atual,
        'anoAtual': ano

    }
    return Render.render('quebra_contrato.html', params, quebra_contrato + '-' + dadoscontrato.numcontrato)

@login_required()
def geracontratoHist(request, id):
    # pega a data atual no formato de ano, mes e dia.
    d = datetime.today().strftime('%y-%m-%d')
    # dados do proprietario
    proprietario = get_object_or_404(proprietarios, userid=request.user.id)
    # variavel do nome da geração do quebra cntrato
    quebra_contrato = 'encerramento'
    # busca os dados do contrato pelo numero do contrato
    dadoscontrato = get_object_or_404(historico_contrato, numcontrato=id)
    # variavel

    # busca os dados do imovel que foi selecionado no contrato.
    dadosimoveis = get_object_or_404(Imovel, id=dadoscontrato.imovel_id)
    # print(dadosimoveis)
    # busca os dados do morador que foi selecionado no contrato
    dadosmorador = get_object_or_404(moradores, nome=dadoscontrato.morador)
    # chama a função number_to_long_number e passa o valor do aluguel para extenso como string.
    aluguel_por_extenso = number_to_long_number(str(dadoscontrato.aluguel))
    data = datetime.today().strftime('%d-%m-%y')
    dia = datetime.today().day
    ano = datetime.today().year
    data_atual = dataExtenso(data)

    # parametros de variaveis para inserir no layout do contrato
    params = {
        'nomeProprietario': proprietario.nome,
        'identidadeProprietario': proprietario.identidade,
        'cpfProprietario': proprietario.cpf,
        'cidadeProprietario': proprietario.cidade,
        'Numcontrato': dadoscontrato.numcontrato,
        'Morador': dadoscontrato.morador,
        'cpfMorador': dadosmorador.cpf,
        'identidadeMorador': dadosmorador.identidade,
        'naturaldeMorador': dadosmorador.natural,
        'estadocivilMorador': dadosmorador.estadocivil,
        'profissaoMorador': dadosmorador.profissao,
        'cependereco': dadosimoveis.cep,
        'Imovel': dadoscontrato.imovel,
        'numeroEndereco': dadosimoveis.numero,
        'bairroEndereco': dadosimoveis.bairro,
        'cidadeEndereco': dadosimoveis.cidade,
        'estadoEndereco': dadosimoveis.estado,
        'Entrada': dadoscontrato.data_entrada,
        'Vencimento': dadoscontrato.vencimento,
        'Aluguel': dadoscontrato.aluguel,
        'Aluguel_extenso': aluguel_por_extenso,
        'diaAtual': dia,
        'mesAtualExtenso': data_atual,
        'anoAtual': ano
    }
    print('dados do contrato', dadoscontrato)
    return Render.render('gerar_contrato.html', params, str(d) + '-' + dadoscontrato.numcontrato)

def dataExtenso(data):

    mes_ext = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',6: 'Junho', 7: 'Julho', 8:'Agosto',
               9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

    dia, mes, ano = data.split("-")
    # print('dia', dia)
    # print('mes', mes_ext[int(mes)])
    # print('ano', ano)
    data_mes = mes_ext[int(mes)]
    return data_mes