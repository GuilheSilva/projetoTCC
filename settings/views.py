from django.shortcuts import render, get_object_or_404, redirect
from imoveis.models import Imovel
from moradores.models import moradores
from proprietario.models import proprietarios
from proprietario.forms import formproprietario
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import xlrd

# homepage de settngs, onde tudo que for adiciionar em settins tem que passar dentro de context=
# senão não vai aparecer no layout
@login_required()
def settings(request):
    #dados = proprietarios.objects.filter(userid=request.user.id)
    dados = proprietarios.objects.get(userid=request.user.id)

    if request.method == 'POST':
        proprietarios.objects.filter(userid=request.user.id).update(nome=request.POST['nome'],
                                                                    identidade=request.POST['identidade'],
                                                                    cpf=request.POST['cpf'],
                                                                    cep=request.POST['cep'],
                                                                    telefone=request.POST['telefone'],
                                                                    endereco=request.POST['endereco'],
                                                                    numero=request.POST['numero'],
                                                                    bairro=request.POST['bairro'],
                                                                    cidade=request.POST['cidade'],
                                                                    estado=request.POST['estado'])
        #dados = proprietarios.objects.get(userid=request.user.id)
        return redirect('settings')
   # print('teste', dados)
    #filename = importForm(request.POST or None)
    return render(request, 'settings/settings.html', context={'dados': dados})

@login_required()
def update_proprietario(request):
    dados = proprietarios.objects.get(userid=request.user.id)
    create = formproprietario(request.POST or None)
    nome = dados.nome
    novonome= 'GuilhermeSilva1'
    nome = novonome

    print('batatinha', nome)
    proprietarios.objects.filter(userid=request.user.id).update(nome=nome)
    return render(request, 'settings/settings.html', context={'dados': dados})



@login_required()
def dados_proprietario(request):
    dados = proprietarios.objects.filter(userid=request.user.id)
    print('batata', dados)


    if request.method == 'POST':
        print('batata frita eh top')
    return render(request, 'settings/dadosProprietario.html', {'dados': dados})

    #return render(request, 'imoveis/realEstate_form.html', {'form': form})

# Aqui gera a  importação do excel ou csv se caso o cliente utilize dessa maneira para controlar
# os seus alugueis.
@login_required()
def import_imoveis(request):
    file = request.FILES['filename']
    files = FileSystemStorage()
    name = files.save(file.name, file)
    path = files.url(name)
    #print(path)
    workbook = xlrd.open_workbook('.'+path)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        status = str(sheet.row(row)[0].value)
        fins = str(sheet.row(row)[1].value)
        endereco = str(sheet.row(row)[2].value)
        numero = int(sheet.row(row)[3].value)
        complemento = str(sheet.row(row)[4].value)
        bairro = str(sheet.row(row)[5].value)
        cidade = str(sheet.row(row)[6].value)
        estado = str(sheet.row(row)[7].value)
        garagem = int(sheet.row(row)[8].value)
        quartos = int(sheet.row(row)[9].value)
        banheiros = int(sheet.row(row)[10].value)
        Imovel.objects.create(status=status, fins=fins, endereco=endereco, numero=numero, complemento=complemento, bairro=bairro,
                              cidade=cidade, estado=estado, garagem=garagem, quartos=quartos,
                              banheiros=banheiros, userid=request.user.id)
    files.delete(file.name)
    # por enquando vai mostrar para a lista do imovel
    posts = Imovel.objects.filter(userid=request.user.id)
  
    return render(request, 'imoveis/imoveis_detail.html', {'posts': posts})
    #return render(request, 'settings/importImoveis.html', {'file': file})

# Aqui gera a  importação do excel ou csv se caso o cliente utilize dessa maneira para controlar
# os seus alugueis.
@login_required()
def import_moradores(request):
    file = request.FILES['filenameMorador']
    files = FileSystemStorage()
    name = files.save(file.name, file)
    path = files.url(name)
    #print(path)
    workbook = xlrd.open_workbook('.'+path)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        nome = str(sheet.row(row)[0].value)
        identidade = str(sheet.row(row)[1].value)
        cpf = str(sheet.row(row)[2].value)
        natural = str(sheet.row(row)[3].value)
        estadocivil = str(sheet.row(row)[4].value)
        profissao = str(sheet.row(row)[5].value)
        email = str(sheet.row(row)[6].value)
        telefone = str(sheet.row(row)[7].value)

        moradores.objects.create(nome=nome, identidade=identidade, cpf=cpf, natural=natural, estadocivil=estadocivil,
                              profissao=profissao, email=email, telefone=telefone, userid=request.user.id)
    files.delete(file.name)
    # por enquando vai mostrar para a lista de moradores
    cliente = moradores.objects.filter(userid=request.user.id)
    return render(request, 'moradores/morador.html', {'cliente': cliente})
    #return render(request, 'settings/importImoveis.html', {'file': file})



