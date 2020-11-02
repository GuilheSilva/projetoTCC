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
from .forms import GeeksForm
from moradores.models import moradores
from .forms import imoveisForm
from imoveis.models import Imovel
from despesas.models import Despesas
from historico.models import historico_contrato
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

def gerar_relatorio_geral(request, data1, data2, option):
    d = datetime.today().strftime('%y-%m-%d')

    contratos = False
    historico = False

    despesas = Despesas.objects.filter(userid=request.user.id,
                                       data__range=[data1, data2])

    if option == 'todos':
        contratos = contrato.objects.filter(userid=request.user.id,
                                            data_entrada__range=[data1, data2], status='Ativo')
        historico = historico_contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[data1, data2], status='Encerrado')
    elif option == 'Ativo':
        contratos = contrato.objects.filter(userid=request.user.id,
                                        data_entrada__range=[data1, data2], status='Ativo')
    else:
        historico = historico_contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[data1, data2], status='Encerrado')


    somaContratos = 0
    somaHistorico = 0

    if contratos:
        for i in contratos:

            recebe_data_post = str(data2)
            pega_data_post = recebe_data_post[0:10]
            d2 = datetime.strptime(pega_data_post, "%Y-%m-%d")

            if d2.date() > i.vencimento:
                dias = abs((i.data_entrada - i.vencimento).days)
            else:
                dias = abs((i.data_entrada - d2.date()).days)
            #dias = abs((d2.date() - d1.date()).days)
            calcula_dias = dias / 30
            arredonda_dias = round(calcula_dias, 1)
            intervaloMeses = int(arredonda_dias)

            somaContratos=somaContratos+(float(i.aluguel) * intervaloMeses)

    if historico:
        for j in historico:
            print(j)
            recebe_data_encerramento = str(j.data_encerramento)
            pega_data_1 = recebe_data_encerramento[0:10]
            data_de_encerramento = datetime.strptime(pega_data_1, "%Y-%m-%d")
            recebe_data_inicial = str(j.data_entrada)
            pega_data_2 = recebe_data_inicial[0:10]
            data_de_inicial = datetime.strptime(pega_data_2, "%Y-%m-%d")
            if d2.date() > data_de_encerramento.date():
                resultado_dias_historico = abs((data_de_encerramento.date() - data_de_inicial.date()).days)
                calcula_dias_historico = resultado_dias_historico / 30
                arredonda_dias_historico = round(calcula_dias_historico, 1)
                intervaloMeses_historico = int(calcula_dias_historico)
            else:
                resultado_dias_historico = abs((d2.date() - data_de_inicial.date()).days)
                calcula_dias_historico = resultado_dias_historico / 30
                arredonda_dias_historico = round(calcula_dias_historico, 1)
                intervaloMeses_historico = int(calcula_dias_historico)

            somaHistorico = somaHistorico + (float(j.aluguel) * intervaloMeses_historico)


    somaDepesas = 0
    for i in despesas:
        somaDepesas = somaDepesas + i.valor

    recebe_data_post1 = str(data1)
    pega_data_post1 = recebe_data_post1[0:10]
    d1 = datetime.strptime(pega_data_post1, "%Y-%m-%d")
    recebe_data_post2 = str(data2)
    pega_data_post2 = recebe_data_post2[0:10]
    d2 = datetime.strptime(pega_data_post2, "%Y-%m-%d")
    dias = abs((d2.date() - d1.date()).days)
    calcula_dias = dias / 30
    arredonda_dias = round(calcula_dias, 1)
    intervaloMeses = int(arredonda_dias)

    data_de_entrada = datetime.strptime(pega_data_post1, "%Y-%m-%d").strftime("%d-%m-%Y")
    data_de_saida = datetime.strptime(pega_data_post2, "%Y-%m-%d").strftime("%d-%m-%Y")

    if historico and contratos:
        somaTotal = (somaContratos+somaHistorico) - float(somaDepesas)
    elif historico:
        somaTotal = somaHistorico- float(somaDepesas)
    elif contratos:
        somaTotal = somaContratos - somaDepesas

    aux = True
    if somaTotal >= 0:
        aux = True
    else:
        aux = False
    params = {
        'despesa': despesas,
        'contratos': contratos,
        'somaTotal': format(somaTotal, '.2f'),
        'somaContratos': format(somaContratos, '.2f'),
        'somaHistorico': format(somaHistorico, '.2f'),
        'somaDespesas': format(somaDepesas, '.2f'),
        'aux':aux,
        'meses':intervaloMeses,
        'data_entrada':data_de_entrada,
        'data_saida':data_de_saida,
        'historico':historico

    }

    return Render.render('relatorio/gerar_relatorio_geral.html', params, str(d)+'-'+'relatorio_geral')

def gerar_relatorio_contratos(request, data1, data2, imovel, opcao):
    # pega a data atual no formato de ano, mes e dia.
    d = datetime.today().strftime('%y-%m-%d')


    if imovel == 0:
        if opcao == 'ativo':
            contrato_object = contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[data1, data2], status='Ativo')
        elif opcao == 'encerrado':
            contrato_object = contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[data1, data2], status='Encerrado')
        else:
            contrato_object = contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[data1, data2])

    else:

        if opcao == 'ativo':
            contrato_object = contrato.objects.filter(userid=request.user.id,
                                                      imovel=imovel,
                                                      data_entrada__range=[data1, data2], status='Ativo')
        elif opcao == 'encerrado':
            contrato_object = contrato.objects.filter(userid=request.user.id,
                                                      imovel=imovel,
                                                      data_entrada__range=[data1, data2], status='Encerrado')
        else:
            contrato_object = contrato.objects.filter(userid=request.user.id,
                                                      imovel=imovel,
                                                      data_entrada__range=[data1, data2])

    somaContratos = 0
    intervaloMeses = 0
    for i in contrato_object:

        recebe_data_post1 = str(data1)
        pega_data_post1 = recebe_data_post1[0:10]
        d1 = datetime.strptime(pega_data_post1, "%Y-%m-%d")
        recebe_data_post2 = str(data2)
        pega_data_post2 = recebe_data_post2[0:10]
        d2 = datetime.strptime(pega_data_post2, "%Y-%m-%d")
        dias = abs((d2.date() - d1.date()).days)
        calcula_dias = dias / 30
        arredonda_dias = round(calcula_dias, 1)
        intervaloMeses = int(arredonda_dias)


        if d2.date() > i.data_entrada:
            dias = abs((i.data_entrada - i.vencimento).days)
        else:
            dias = abs((i.data_entrada - d2.date()).days)

        somaContratos = somaContratos + (float(i.aluguel) * intervaloMeses)

    data_de_entrada = datetime.strptime(pega_data_post1, "%Y-%m-%d").strftime("%d-%m-%Y")
    data_de_saida = datetime.strptime(pega_data_post2, "%Y-%m-%d").strftime("%d-%m-%Y")


    # parametros de variaveis para inserir no layout do contrato
    params = {
        'contratos': contrato_object,
        'somaContratos':somaContratos,
        'meses': intervaloMeses,
        'data_de_entrada': data_de_entrada,
        'data_de_saida': data_de_saida
    }
    print(params)
    return Render.render('relatorio/gerar_relatorio_contrato.html', params, str(d)+'-'+'relatorio_contrato')

def gerar_relatorio_despesas(request, data1, data2, imovel, opcao):

    d = datetime.today().strftime('%y-%m-%d')
    print(type(opcao))
    if opcao == 'todos':
        if imovel == 0:
            despesas = Despesas.objects.filter(userid=request.user.id,
                                               data__range=[data1, data2])
        else:
            despesas = Despesas.objects.filter(userid=request.user.id, imoveis=imovel,
                                               data__range=[data1, data2])
    else:
        if imovel == 0:
            despesas = Despesas.objects.filter(userid=request.user.id,
                                               data__range=[data1, data2], tipo=opcao)
        else:
            despesas = Despesas.objects.filter(userid=request.user.id, imoveis=imovel,
                                               data__range=[data1, data2], tipo=opcao)

    recebe_data_post1 = str(data1)
    pega_data_post1 = recebe_data_post1[0:10]
    d1 = datetime.strptime(pega_data_post1, "%Y-%m-%d")
    recebe_data_post2 = str(data2)
    pega_data_post2 = recebe_data_post2[0:10]
    d2 = datetime.strptime(pega_data_post2, "%Y-%m-%d")
    dias = abs((d2.date() - d1.date()).days)
    calcula_dias = dias / 30
    arredonda_dias = round(calcula_dias, 1)
    intervaloMeses = int(arredonda_dias)

    data_de_entrada = datetime.strptime(pega_data_post1, "%Y-%m-%d").strftime("%d-%m-%Y")
    data_de_saida = datetime.strptime(pega_data_post2, "%Y-%m-%d").strftime("%d-%m-%Y")


    somaDespesas = 0
    for i in despesas:
        somaDespesas = somaDespesas + float(i.valor)

    params = {

        'despesa': despesas,
        'somaDespesas': somaDespesas,
        'meses':intervaloMeses,
        'data_de_entrada':data_de_entrada,
        'data_de_saida':data_de_saida

    }

    return Render.render('relatorio/gerar_relatorio_despesas.html', params, str(d) + '-' + 'relatorio_despesas')

def relatorio_contratos(request):

    imoveis  = Imovel.objects.filter(userid=request.user.id)

    var = list(map(lambda x: (x.id, (x.endereco + ', ' + str(x.numero) + ', ' + str(x.complemento))), imoveis))
    var.append(('', 'Todos'))
    geeks_field = forms.ChoiceField(choices=var)


    if request.method == "GET":
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field

        options = GeeksForm()

        return render(request, 'relatorio/relatorio_contratos_form.html', {'form': form, 'options':options})

    if request.method == 'POST':

        if request.POST['imovel'] == '':
            if request.POST['opcoes_contrato'] == 'ativo':
                contrato_object = contrato.objects.filter(userid=request.user.id,data_entrada__range=[request.POST['data1'], request.POST['data2']], status='Ativo')
            elif request.POST['opcoes_contrato'] == 'encerrado':
                contrato_object = contrato.objects.filter(userid=request.user.id,
                                                          data_entrada__range=[request.POST['data1'],
                                                                               request.POST['data2']], status='Encerrado')
            else:
                contrato_object = contrato.objects.filter(userid=request.user.id,
                                                          data_entrada__range=[request.POST['data1'],
                                                                               request.POST['data2']])
        else:
            if request.POST['opcoes_contrato'] == 'ativo':
                contrato_object = contrato.objects.filter(userid=request.user.id, imovel=request.POST['imovel'],
                                                          data_entrada__range=[request.POST['data1'],
                                                                               request.POST['data2']], status='Ativo')
            elif request.POST['opcoes_contrato'] == 'encerrado':
                contrato_object = contrato.objects.filter(userid=request.user.id, imovel=request.POST['imovel'],
                                                          data_entrada__range=[request.POST['data1'],
                                                                               request.POST['data2']], status='encerrado')
            else:
                contrato_object = contrato.objects.filter(userid=request.user.id, imovel=request.POST['imovel'],
                                                          data_entrada__range=[request.POST['data1'],
                                                                               request.POST['data2']])
        somaContratos = 0
        intervaloMeses=0
        for i in contrato_object:

            recebe_data_post = str(request.POST['data2'])
            pega_data_post = recebe_data_post[0:10]
            d2 = datetime.strptime(pega_data_post, "%Y-%m-%d")

            if d2.date() > i.vencimento:
                dias = abs((i.data_entrada - i.vencimento).days)
            else:
                dias = abs((i.data_entrada - d2.date()).days)

            calcula_dias = dias/30
            arredonda_dias = round(calcula_dias,1)
            intervaloMeses = int(arredonda_dias)
            somaContratos = somaContratos + (float(i.aluguel) * intervaloMeses)

        recebe_data_post1 = str(request.POST['data1'])
        pega_data_post1 = recebe_data_post1[0:10]
        d1 = datetime.strptime(pega_data_post1, "%Y-%m-%d")
        recebe_data_post2 = str(request.POST['data2'])
        pega_data_post2 = recebe_data_post2[0:10]
        d2 = datetime.strptime(pega_data_post2, "%Y-%m-%d")
        dias = abs((d2.date() - d1.date()).days)
        calcula_dias = dias / 30
        arredonda_dias = round(calcula_dias, 1)
        intervaloMeses = int(arredonda_dias)
        mostrar_lista = True
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field
        if request.POST['imovel'] == '':
            aux = 0
        else:
            aux = request.POST['imovel']

        if request.POST['opcoes_contrato'] == 'ativo':
            opcao = 'ativo'
        elif request.POST['opcoes_contrato'] == 'encerrado':
            opcao = 'encerrado'
        else:
            opcao = 'todos'

        data_de_entrada = datetime.strptime(pega_data_post1, "%Y-%m-%d").strftime("%d-%m-%Y")
        data_de_saida = datetime.strptime(pega_data_post2, "%Y-%m-%d").strftime("%d-%m-%Y")


        context = {
            'form':form,
            'contratos':contrato_object,
            'somaContratos':somaContratos,
            'mostrar_lista':mostrar_lista,
            'data1':request.POST['data1'],
            'data2':request.POST['data2'],
            'imovel':aux,
            'opcao':opcao,
            'meses':intervaloMeses,
            'data_de_entrada': data_de_entrada,
            'data_de_saida': data_de_saida

        }
        return render(request, 'relatorio/relatorio_contratos_form.html', context=context)

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

        if request.POST['opcoes_despesa'] == 'todos':
             if request.POST['imovel'] == '':
                despesas = Despesas.objects.filter(userid=request.user.id, data__range=[request.POST['data1'], request.POST['data2']])
             else:
                despesas = Despesas.objects.filter(userid=request.user.id, imoveis=request.POST['imovel'], data__range=[request.POST['data1'], request.POST['data2']])
        else:
             if request.POST['imovel'] == '':
                despesas = Despesas.objects.filter(userid=request.user.id, data__range=[request.POST['data1'], request.POST['data2']], tipo=request.POST['opcoes_despesa'])
             else:
                despesas = Despesas.objects.filter(userid=request.user.id, imoveis=request.POST['imovel'], data__range=[request.POST['data1'], request.POST['data2']], tipo=request.POST['opcoes_despesa'])

        somaDespesas = 0
        intervaloMeses = 0
       # for i in despesas:
        recebe_data_post1= str(request.POST['data1'])
        pega_data_post1 = recebe_data_post1[0:10]
        d1 = datetime.strptime(pega_data_post1, "%Y-%m-%d")
        recebe_data_post2 = str(request.POST['data2'])
        pega_data_post2 = recebe_data_post2[0:10]
        d2 = datetime.strptime(pega_data_post2, "%Y-%m-%d")

        dias = abs((d2.date() - d1.date()).days)

        calcula_dias = dias/30
        arredonda_dias = round(calcula_dias,1)
        intervaloMeses = int(arredonda_dias)


        for i in despesas:
            somaDespesas = somaDespesas + float(i.valor)
        print(somaDespesas)
        mostrar_lista = True
        form = imoveisForm(request.GET or None)
        form.fields['imovel'] = geeks_field

        if request.POST['imovel'] == '':
            aux = 0
        else:
            aux = request.POST['imovel']
        opcao = ''
        if request.POST['opcoes_despesa'] == 'todos':
            opcao = 'todos'
        else:
            opcao = request.POST['opcoes_despesa']

        data_de_entrada = datetime.strptime(pega_data_post1, "%Y-%m-%d").strftime("%d-%m-%Y")
        data_de_saida = datetime.strptime(pega_data_post2, "%Y-%m-%d").strftime("%d-%m-%Y")

        print(data_de_saida)
        context = {
            'form':form,
            'despesa':despesas,
            'somaDespesas':somaDespesas,
            'mostrar_lista':mostrar_lista,
            'data1':request.POST['data1'],
            'data2':request.POST['data2'],
            'imovel':aux,
            'opcao':opcao,
            'meses':intervaloMeses,
            'data_de_entrada': data_de_entrada,
            'data_de_saida': data_de_saida
        }
        return render(request, 'relatorio/relatorio_despesas_form.html', context=context)

def relatorio_geral(request):
    historico = False
    contratos=False
    if request.method == 'POST':
        #print(request.POST['select'])
        print(request.POST['opcoes_contrato'])
        if request.POST['opcoes_contrato'] == 'ativo':
            contratos = contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[request.POST['data1'],
                                                                           request.POST['data2']], status='Ativo')
            despesas = Despesas.objects.filter(userid=request.user.id,
                                               data__range=[request.POST['data1'], request.POST['data2']])
        elif request.POST['opcoes_contrato'] == 'encerrado':
            historico = historico_contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[request.POST['data1'],
                                                                           request.POST['data2']], status='Encerrado')
            despesas = Despesas.objects.filter(userid=request.user.id,
                                               data__range=[request.POST['data1'], request.POST['data2']])
        else:
            contratos = contrato.objects.filter(userid=request.user.id,
                                                      data_entrada__range=[request.POST['data1'],
                                                                           request.POST['data2']], status='Ativo')
            historico = historico_contrato.objects.filter(userid=request.user.id,
                                                          data_entrada__range=[request.POST['data1'],
                                                                               request.POST['data2']],)
            despesas = Despesas.objects.filter(userid=request.user.id,
                                               data__range=[request.POST['data1'], request.POST['data2']])

        mostrar_lista = True
        intervaloMeses = 0
        somaContratos=0
        somaHistorico=0
        if historico:
            for j in historico:
                print(j)
                recebe_data_encerramento = str(j.data_encerramento)
                pega_data_1 = recebe_data_encerramento[0:10]
                data_de_encerramento = datetime.strptime(pega_data_1, "%Y-%m-%d")
                recebe_data_inicial = str(j.data_entrada)
                pega_data_2 = recebe_data_inicial[0:10]
                recebe_data_post = str(request.POST['data2'])
                pega_data_post = recebe_data_post[0:10]
                d2 = datetime.strptime(pega_data_post, "%Y-%m-%d")
                data_de_inicial = datetime.strptime(pega_data_2, "%Y-%m-%d")

                if d2.date() > data_de_encerramento.date():
                    resultado_dias_historico= abs((data_de_encerramento.date() - data_de_inicial.date()).days)
                    calcula_dias_historico=resultado_dias_historico/30
                    arredonda_dias_historico = round(calcula_dias_historico, 1)
                    intervaloMeses_historico = int(calcula_dias_historico)
                else:
                    resultado_dias_historico = abs((d2.date() - data_de_inicial.date()).days)
                    calcula_dias_historico = resultado_dias_historico / 30
                    arredonda_dias_historico = round(calcula_dias_historico, 1)
                    intervaloMeses_historico = int(calcula_dias_historico)
                somaHistorico = somaHistorico + (float(j.aluguel) * intervaloMeses_historico)


        if contratos:
            for i in contratos:
                recebe_data_post = str(request.POST['data2'])
                pega_data_post = recebe_data_post[0:10]
                d2 = datetime.strptime(pega_data_post, "%Y-%m-%d")

                if d2.date() > i.vencimento:
                    dias = abs((i.data_entrada - i.vencimento).days)
                else:
                    dias = abs((i.data_entrada - d2.date()).days)

                calcula_dias = dias / 30
                arredonda_dias = round(calcula_dias, 1)
                intervaloMeses = int(arredonda_dias)
                somaContratos = somaContratos + (float(i.aluguel) * intervaloMeses)



        somaDepesas=0
        for i in despesas:
            somaDepesas = somaDepesas + float(i.valor)


        recebe_data_post1 = str(request.POST['data1'])
        pega_data_post1 = recebe_data_post1[0:10]
        d1 = datetime.strptime(pega_data_post1, "%Y-%m-%d")
        recebe_data_post2 = str(request.POST['data2'])
        pega_data_post2 = recebe_data_post2[0:10]
        d2 = datetime.strptime(pega_data_post2, "%Y-%m-%d")
        dias = abs((d2.date() - d1.date()).days)
        calcula_dias = dias / 30
        arredonda_dias = round(calcula_dias, 1)
        intervaloMeses = int(arredonda_dias)

        data_de_entrada = datetime.strptime(pega_data_post1, "%Y-%m-%d").strftime("%d-%m-%Y")
        data_de_saida = datetime.strptime(pega_data_post2, "%Y-%m-%d").strftime("%d-%m-%Y")
       # if historico:

        print(' - '*20, somaHistorico)
        somaTotal = (somaContratos+somaHistorico) - somaDepesas
       # else:
       #     somaTotal = somaContratos - somaDepesas
        verifica = True
        if somaTotal >=0:
            verifica = True
        else:
            verifica = False
        auxiliar = ' '
        if request.POST['opcoes_contrato'] == '':
            auxiliar = 'todos'
        else:
            auxiliar = request.POST['opcoes_contrato']

        context = {
            'despesa':despesas,
            'contratos':contratos,
            'somaTotal':format(somaTotal, '.2f'),
            'somaContratos':format(somaContratos, '.2f'),
            'somaHistorico':format(somaHistorico, '.2f'),
            'somaDespesas':format(somaDepesas, '.2f'),
            'mostrar_lista':mostrar_lista,
            'data1':request.POST['data1'],
            'data2':request.POST['data2'],
            'verifica':verifica,
            'meses':intervaloMeses,
            'data_inicial':data_de_entrada,
            'data_final':data_de_saida,
            'historico':historico,
            'option':auxiliar

        }

        #return render(request, 'relatorio/relatorio_geral_form.html', {'despesa': despesas,'contratos':contratos, 'somaTotal':format(somaTotal, '.2f'),'somaContratos':format(somaContratos, '.2f'), 'somaDepesas':format(somaDepesas, '.2f'),'mostrar_lista':mostrar_lista} )
        return render(request, 'relatorio/relatorio_geral_form.html', context=context)

    return render(request, 'relatorio/relatorio_geral_form.html')
    #return render(request, 'relatorio/teste.html')



