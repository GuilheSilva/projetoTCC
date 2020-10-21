import io
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from .models import (contrato, document,imagem)
from datetime import datetime
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from .forms import (contratoform,
                    documentform,
                    photoform)
from .models import Imovel
from .models import moradores
from django import forms
from contratos.models import geracaoNumContrato
from num2words import num2words

# Nessa função lista os contratos gerados no sistema
@login_required()
def lista_contratos(request):
    model = contrato
    contratos = contrato.objects.filter(userid=request.user.id, status='Ativo')
    return render(request, 'contratos.html', {'contratos': contratos})

# nessa função é realizado a criação do contrato
@login_required()
def create_contrato(request):

    imoveis = Imovel.objects.filter(status='Desocupado')
   # var = list(map(lambda x:(x.id,x.endereco),imoveis))
    var = list(map(lambda x: (x.id, (x.endereco + ', '+ str(x.numero) + ', ' + str(x.complemento))), imoveis))
    var.append(('','selecione uma opcao'))
    geeks_field = forms.ChoiceField(choices=var)

    morador = moradores.objects.filter(userid=request.user.id)
    var2 = list(map(lambda x: (x.id, x.nome), morador))
    var2.append(('', 'selecione uma opcao'))
    lista_morador = forms.ChoiceField(choices=var2)

    if request.method == "GET":
        form = contratoform(request.GET or None)
        form.fields['imovel'] = geeks_field
        form.fields['morador'] = lista_morador
        return render(request,  'contratos_form.html',
                      {'form': form, 'id': geracaoNumContrato()})
    else:
        form = contratoform(request.POST or None)
        #print(form.is_valid)
        if form.is_valid():
            numcontrato = form.cleaned_data['numcontrato']
            aluguel = form.cleaned_data['aluguel']
            imovel = form.cleaned_data['imovel']
            morador = form.cleaned_data['morador']
            status = form.cleaned_data['status']
            data_entrada = form.cleaned_data['data_entrada']
            vigencia = form.cleaned_data['vigencia']
            vencimento = form.cleaned_data['vencimento']

            contrato.objects.create(numcontrato=numcontrato, aluguel=aluguel, imovel=imovel,
                                    morador=morador, data_entrada=data_entrada, vigencia=vigencia,
                                    vencimento=vencimento, status=status, userid=request.user.id)
            i = int(imovel.id)
            filtro = Imovel.objects.filter(id=i).update(status='Alugado')
            return redirect('listagem_contratos')
        form.fields['imovel'] = geeks_field
        form.fields['morador'] = lista_morador
        #print(form)
        return render(request, 'contratos_form.html', {'form': form})

@login_required()
def encerra_contrato(request, id):
    numcontrato = get_object_or_404(contrato, numcontrato=id)
    if request.method == 'POST':
        contrato.objects.filter(numcontrato=numcontrato).update(status='Encerrado')
        id_imovel = contrato.objects.filter(numcontrato=numcontrato)
        var = list(map(lambda x: (x.imovel_id), id_imovel))
        Imovel.objects.filter(id=var[0]).update(status='Desocupado')
        return redirect('listagem_contratos')
    return render(request, 'confirmacao_de_encerramento.html', {'numcontrato': numcontrato})

# teste
def imovel(imoveis):
    validos = []
    #print(imoveis)
    for imovel in imoveis:
        if imovel.status == 'Desocupado':
            validos.append(imovel)
    #print(validos)
    return validos
#-----------------------------------------------------------------

# essa função mostra os detalhes do contrato que foi gerado
@login_required()
def contratoDetail(request, id):
    doclist = document.objects.filter(contrato=id)
    pholist = imagem.objects.filter(contrato=id)
    contratos = get_object_or_404(contrato, numcontrato=id)
    return render(request, 'contratoDetail.html', context={'contratos': contratos,
                                                           'doclist': doclist,
                                                           'pholist': pholist})

#---------------------------------------------------------------------------------

# essa função mostra os documentos anexados no contrato
def doc_list(request, id):
    doclist = document.objects.filter(contrato=id)
    return render(request, 'documentoView.html', {'doclist': doclist})

# essa função anexa os documentos ao contrato gerado
def doc_contrato(request, id):
    doc = documentform(request.POST or None, request.FILES or None)
    if doc.is_valid():
        teste = doc.save(commit=False)
        teste.contrato = contrato.objects.get(numcontrato=id)
        #print(teste.contrato)
        teste.save()
        return redirect('/contrato/detalhe_contrato/' + str(id))
    return render(request, 'documento.html', {'doc': doc})

# essa função deleta o documento do contrato
def doc_delete(request, id):
    docs=get_object_or_404(document,pk=id)
    if request.method == 'POST':
        docs.delete()
        return redirect('detalhe_contrato/' + str(id))
    return render(request, 'documento_delete_confirm.html', {'docs': docs})

#---------------------------------------------------------------------------

# nessa função faz a listagem das fotos anexados no contrato.
def photo_view(request, id):
    pholist = imagem.objects.filter(contrato=id)
    return render(request, 'photo_view.html', {'pholist': pholist})

# nessa função anexa as fotos no contrato
def photo_create(request, id):
    photo = photoform(request.POST or None, request.FILES or None)
    if photo.is_valid():
        teste = photo.save(commit=False)
        teste.contrato = contrato.objects.get(numcontrato=id)
        teste.save()
        return redirect('/contrato/detalhe_contrato/' + str(id))
    return render(request, 'photo_form.html', {'photo': photo})

#-------------------------------------------------------------------
# essa função é utilizda na geracontrato onde o valor do aluguel é por extenso.
def number_to_long_number(number_p):
    if number_p.find(',') != 0:
        number_p = number_p.split('.')

        number_p1 = int(number_p[0].replace('.',''))

        number_p2 = int(number_p[1])
    else:
        number_p1 = int(number_p.replace('.',''))
        number_p2 = 0

    if number_p1 == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'

    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'

    text1 = ''
    if number_p1 > 0:
        text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
    else:
        text1 = ''

    if number_p2 > 0:
        text2 = num2words(number_p2,lang='pt_BR') + str(aux2)
    else:
        text2 = ''

    if (number_p1 > 0 and number_p2 > 0):
        result = text1 + ' e ' + text2
    else:
        result = text1 + text2
    return result

#--------------------------------------------------------------------

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
def geracontrato(request,id):
    # pega a data atual no formato de ano, mes e dia.
    d = datetime.today().strftime('%y-%m-%d')
    # busca os dados do contrato pelo numero do contrato
    dadoscontrato = get_object_or_404(contrato, numcontrato=id)
    # busca os dados do imovel que foi selecionado no contrato.
    dadosimoveis = get_object_or_404(Imovel,id=dadoscontrato.imovel_id)
    #print(dadosimoveis)
    # busca os dados do morador que foi selecionado no contrato
    dadosmorador = get_object_or_404(moradores, id=dadoscontrato.morador_id)
    #chama a função number_to_long_number e passa o valor do aluguel para extenso como string.
    aluguel_por_extenso = number_to_long_number(str(dadoscontrato.aluguel))
    #print(aluguel_por_extenso)

    # params1{
    #     dadosimoveis.numero
    # }

    # parametros de variaveis para inserir no layout do contrato
    params = {
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
        'Aluguel_extenso': aluguel_por_extenso
    }
    print(params)
    return Render.render('gerar_contrato.html', params, str(d)+'-'+dadoscontrato.numcontrato)
