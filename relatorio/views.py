import io
from django.db.models import Q
from datetime import datetime
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.utils.translation import gettext as _
from reportlab.pdfgen import canvas
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from contratos.models import contrato
from contratos.views import number_to_long_number
from despesas.models import Despesas
from reportlab.lib.pagesizes import A4
from django.shortcuts import render, get_object_or_404
from django import forms

from moradores.models import moradores
from .forms import imoveisForm
from imoveis.models import Imovel
from despesas.models import Despesas
# se vc quiser criar aqui o calculo dos valore de despesas, vc pode usar essa função como exemplo
# Coloquei o mesmo calculo na app de Despesas.
# acho que essa função já te ajuda, no caso do Gregory, ele criou no models.
# Acho que aqui ou em Despesas já faz o calculo correto.

#https://github.com/Gpzim98/gestao_clientes/blob/advanced/vendas/models.py

# def calcular_total(self):
#     tot = self.itemdopedido_set.all().aggregate(
#         tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
#     )['tot_ped'] or 0
#
#     tot = tot - float(self.impostos) - float(self.desconto)
#     self.valor = tot
#     Venda.objects.filter(id=self.id).update(valor=tot)
#
#
# def __str__(self):
#     return self.numero

def relatorio_contratos_pdf(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    d = datetime.today().strftime('%y-%m-%d')
    response['Content_Disposition'] = 'attachment; filename ="{d}.pdf"'
    # Criado o objeto PDF, usando o objeto response como "arquivo".
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    p.drawString(45, 740, "Contratos")
    p.drawString(180, 740, "Morador")
    p.drawString(380, 740, "Imovel")
    p.drawString(520, 740, "Valor")
    p.drawString(45, 710, "Data de entrada")
    p.drawString(180, 710, "Vigencia")
    p.drawString(280, 710, "Vencimento")
    p.drawString(40, 700, "_______________________________________________________________________________")

    p.setFont("Helvetica", 12, leading=None)
    # p.setFillColorRGB(0.29296875,0.453125,0.609375)
    p.drawString(210, 800, "Relatorio de contratos gerados")
    p.line(0, 780, 1000, 780)

    y = 670
    quebraLinha = 620
    y2=640
    contratos = contrato.objects.filter(userid=request.user.id)
    str = '%s'
    for c in contratos:
        print('----------------------------'*10)
        print(c.aluguel)
        aluguel = float(c.aluguel)
        print(type(aluguel))
        p.drawString(50, y, str % (c.numcontrato))
        p.drawString(180, y, str % (c.morador))
        p.drawString(380, y, str % (c.imovel))
        p.drawString(520, y, str % (c.aluguel))
        p.drawString(50, y2, str % (c.data_entrada))
        p.drawString(195, y2, str % (c.vigencia))
        p.drawString(280, y2, str % (c.vencimento))
        p.drawString(40, quebraLinha, str % "__________________________"
                                            "___________________________"
                                            "__________________________")
        y -= 80
        y2 -= 80
        quebraLinha -= 80

    p.setTitle(f'Relatorio - {d}')
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
def despesas_relatorio(request):

    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    d = datetime.today().strftime('%y-%m-%d')
    response['Content_Disposition'] = 'attachment; filename ="{d}.pdf"'
    # Criado o objeto PDF, usando o objeto response como "arquivo".
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    p.drawString(65, 740, "Imovel")
    p.drawString(300, 740, "Data")
    p.drawString(390, 740, "Tipo")
    p.drawString(510, 740, "Valor")
    p.drawString(55, 720, "Observacao")
    p.drawString(30, 710, "______________________________________________________________________________")

    p.setFont("Helvetica", 12, leading=None)
    # p.setFillColorRGB(0.29296875,0.453125,0.609375)
    p.drawString(210, 800, "Relatorio de despesas gerado")
    p.line(0, 780, 1000, 780)

    y = 685
    quebraLinha = 655
    y2=668
    despesas = Despesas.objects.filter(userid=request.user.id)
    print(despesas)
    str = '%s'
    somatotal=0
    for c in despesas:
        #p.drawString(45, 740, "Imovel")
        #infoImovel =  str % (c.imoveis)
        #infoImovel = infoImovel + ', ' + str % (c.numero)
        #infoImovel = infoImovel + ', ' + str % (c.complemento)

        p.drawString(30, y, str % (c.imoveis))

        valor = str % (c.valor)
        valor = "R$ " + valor
        somaValor = float(c.valor)
        somatotal = somaValor + somatotal

        p.drawString(300, y, (c.data.strftime('%d/%m/%Y')))
        p.drawString(390, y, str % (c.tipo))
        p.drawString(510, y, str % valor)
        p.drawString(30, y2, str % (c.observacao))
        p.drawString(30, quebraLinha, str % "__________________________"
                                            "___________________________"
                                            "__________________________")
        y -= 60
        y2 -= 60
        quebraLinha -= 60

    p.drawString(345, y, "Total: ")
    total = str % (somatotal)
    total = "R$ " + total
    p.drawString(380, y, total)

    p.setTitle(f'Relatorio - {d}')
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str, date_entrada, date_saida):
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



def geracontrato(request):
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

    # parametros de variaveis para inserir no layout do contrato
    params = {
        'Numcontrato': dadoscontrato.numcontrato,
        'Morador': dadoscontrato.morador,
        'cpfMorador': dadosmorador.cpf,
        'identidadeMorador': dadosmorador.identidade,
        'naturaldeMorador': dadosmorador.natural,
        'estadocivilMorador': dadosmorador.estadocivil,
        'profissaoMorador': dadosmorador.profissao,
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
    return Render.render('gerar_contrato.html', params, str(d)+'-'+dadoscontrato.numcontrato,date_entrada, date_saida)

def gerar_relatorio_pdf(request, data1, data2):

    despesa = Despesas.objects.filter(data__range=[data1, data2])


    return render(request, 'relatorio/relatorio_geral_form.html', {'despesa': despesa})


def relatorio_contratos(request):

    imoveis  = Imovel.objects.filter(userid=request.user.id)

    var = list(map(lambda x: (x.id, (x.endereco + ', ' + str(x.numero) + ', ' + str(x.complemento))), imoveis))
    var.append(('', 'Todos'))
    geeks_field = forms.ChoiceField(choices=var)
    print(geeks_field)

    if request.method == "GET":
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field
        print(form)

        return render(request, 'relatorio/relatorio_contratos_form.html', {'form': form})

    if request.method == 'POST':
        print(request.POST['data1'])
        print(request.POST['data2'])
        print(request.POST['imovel'])

        if request.POST['imovel'] == '':
            contrato_object = contrato.objects.filter(userid=request.user.id,data_entrada__range=[request.POST['data1'], request.POST['data2']])
        else:
            contrato_object = contrato.objects.filter(userid=request.user.id, imovel=request.POST['imovel'], data_entrada__range=[request.POST['data1'], request.POST['data2']])

        somaContratos = 0
        for i in contrato_object:
            somaContratos = somaContratos + float(i.aluguel)
        mostrar_lista = True
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field

        context = {
            'form':form,
            'contratos':contrato_object,
            'somaContratos':somaContratos,
            'mostrar_lista':mostrar_lista,
            'data1':request.POST['data1'],
            'data2':request.POST['data2'],

        }
        return render(request, 'relatorio/relatorio_contratos_form.html', context=context)


def print_relatorio(request, date1):
    print(request)



def relatorio_despesas(request):

    imoveis  = Imovel.objects.filter(userid=request.user.id)

    var = list(map(lambda x: (x.id, (x.endereco + ', ' + str(x.numero) + ', ' + str(x.complemento))), imoveis))
    var.append(('', 'Todos'))
    geeks_field = forms.ChoiceField(choices=var)
    print(geeks_field)

    if request.method == "GET":
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field
        print(form)

        return render(request, 'relatorio/relatorio_despesas_form.html', {'form': form})

    if request.method == 'POST':
        print(request.POST['data1'])
        print(request.POST['data2'])
        print(request.POST['imovel'])

        if request.POST['imovel'] == '':
            despesas = Despesas.objects.filter(userid=request.user.id,data__range=[request.POST['data1'], request.POST['data2']])
        else:
            despesas = Despesas.objects.filter(userid=request.user.id, imoveis=request.POST['imovel'], data__range=[request.POST['data1'], request.POST['data2']])

        somaDespesas = 0
        for i in despesas:
            somaDespesas = somaDespesas + float(i.valor)
        print(somaDespesas)
        mostrar_lista = True
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field

        context = {
            'form':form,
            'despesa':despesas,
            'somaDespesas':somaDespesas,
            'mostrar_lista':mostrar_lista,

        }
        return render(request, 'relatorio/relatorio_despesas_form.html', context=context)



def relatorio_geral(request):

    if request.method == 'POST':
        #print(request.POST['select'])

        despesas = Despesas.objects.filter(userid=request.user.id, data__range=[request.POST['data1'], request.POST['data2']])
        contratos = contrato.objects.filter(userid=request.user.id, data_entrada__range=[request.POST['data1'], request.POST['data2']])

        mostrar_lista = True
        somaContratos=0
        for i in contratos:
            somaContratos = somaContratos + float(i.aluguel)
        somaDepesas=0
        for i in despesas:
            somaDepesas = somaDepesas + float(i.valor)

        somaTotal = somaContratos - somaDepesas
        context = {
            'despesa':despesas,
            'contratos':contratos,
            'somaTotal':format(somaTotal, '.2f'),
            'somaContratos':format(somaContratos, '.2f'),
            'somaDespesas':format(somaDepesas, '.2f'),
            'mostrar_lista':mostrar_lista,

        }

        #return render(request, 'relatorio/relatorio_geral_form.html', {'despesa': despesas,'contratos':contratos, 'somaTotal':format(somaTotal, '.2f'),'somaContratos':format(somaContratos, '.2f'), 'somaDepesas':format(somaDepesas, '.2f'),'mostrar_lista':mostrar_lista} )
        return render(request, 'relatorio/relatorio_geral_form.html', context=context)

    return render(request, 'relatorio/relatorio_geral_form.html')
    #return render(request, 'relatorio/teste.html')



