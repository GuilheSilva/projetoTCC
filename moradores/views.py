from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import moradores
from .forms import moradorForm
#from django.utils import timezone

@login_required()
def residents_list(request):
    cliente = moradores.objects.filter(userid=request.user.id)
    return render(request, 'moradores/morador.html', {'cliente': cliente})

@login_required()
def residents_new(request):
    form = moradorForm(request.POST or None)
    if form.is_valid():
        teste = form.save(commit=False)
        teste.userid = request.user.id
        teste.save()
        return redirect('lista_moradores')
    return render(request, 'moradores/morador_form.html', {'form': form})

@login_required()
def residents_update(request, id):
    cliente = get_object_or_404(moradores, pk=id)
    form = moradorForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_moradores')
    return render(request, 'moradores/morador_form.html', {'form':form})

@login_required()
def residents_delete(request, id):
    cliente = get_object_or_404(moradores, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_moradores')
    return render(request, 'moradores/morador_delete_confirm.html', {'cliente':cliente})

@login_required()
def voltarMorador(request):
    return redirect('lista_moradores')

