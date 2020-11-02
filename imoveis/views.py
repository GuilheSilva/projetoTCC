from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Imovel
from .forms import ImoveisForm
from django.contrib import messages
import xlrd

@login_required()
def realEstate_list(request):
    posts = Imovel.objects.filter(userid=request.user.id)
    return render(request, 'imoveis/imoveis_detail.html', {'posts': posts})

@login_required()
def realEstate_new(request):
    form = ImoveisForm(request.POST or None)
    #print(form.is_valid)
    if form.is_valid():
        # #form.save()
        # teste = form.save(commit=False)
        # teste.userid = request.user.id
        # teste.save()

        status = form.cleaned_data['status']
        fins = form.cleaned_data['status']
        cep = form.cleaned_data['cep']
        endereco = form.cleaned_data['endereco']
        numero = form.cleaned_data['numero']
        complemento = form.cleaned_data['complemento']
        bairro = form.cleaned_data['bairro']
        cidade = form.cleaned_data['cidade']
        estado = form.cleaned_data['estado']
        garagem = form.cleaned_data['garagem']
        quartos = form.cleaned_data['quartos']
        banheiros = form.cleaned_data['banheiros']



        Imovel.objects.create(status=status, fins=fins, cep=cep, endereco=endereco, numero=numero,
                              complemento=complemento, bairro=bairro, cidade=cidade, estado=estado,
                              garagem=garagem, quartos= quartos, banheiros=banheiros, userid=request.user.id)
        return redirect('realEstate_listing')

    #print(form)
    return render(request, 'imoveis/realEstate_form.html', {'form': form})

@login_required()
def realEstate_update(request, id):
    realEstate = get_object_or_404(Imovel, pk=id)
    form = ImoveisForm(request.POST or None, instance=realEstate)

    if form.is_valid():
        form.save()
        return redirect('realEstate_listing')
    return render(request, 'imoveis/realEstate_form.html', {'form': form})

@login_required()
def realEstate_delete(request, id):
    realEstate = get_object_or_404(Imovel, pk=id)

    if request.method == 'POST':
        try:
            realEstate.delete()
        except Exception as e:
            messages.error(request, f"Não foi possível excluir o imóvel {realEstate}, pois ele faz parte de um contrato!")
            return redirect('realEstate_listing')
    return render(request, 'imoveis/realEstate_delete_confirm.html', {'realEstate': realEstate})


@login_required()
def voltar(request):
    return redirect('realEstate_listing')

