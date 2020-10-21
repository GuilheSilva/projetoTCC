from django.shortcuts import render, redirect, get_object_or_404
from imoveis.models import Imovel
from .forms import despesasForm
from .models import Despesas
from django import forms
from django.contrib.auth.decorators import login_required

@login_required
def despesas_edit(request, id):
    editDespesa = get_object_or_404(Despesas, pk=id)
    form = despesasForm(request.POST or None, instance=editDespesa)
    print(form['imoveis'])
    if form.is_valid():
        form.save()
        return redirect('despesas_list')
    return render(request, 'despesas/despesas_form.html', {'despesa':form})


@login_required
def despesas_new(request):
    #"""
    imoveis = Imovel.objects.filter(userid=request.user.id)
    print(imoveis)
    var = list(map(lambda x: (x.id, (x.endereco + ', '+ str(x.numero) + ', ' + str(x.complemento))), imoveis))
   # var = list(map(lambda x: (x.id, (x.numero)), imoveis))
    print(var)
    var.append(('', 'selecione uma opcao'))
    print(var)
    geeks_field = forms.ChoiceField(choices=var)
    if request.method == "GET":

        form = despesasForm(request.GET or None)
        form.fields['imoveis'] = geeks_field


        return render(request, 'despesas/despesas_form.html', {'despesa': form})
    else:

        form = despesasForm(request.POST or None)
        print(form['imoveis'])
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            valor = form.cleaned_data['valor']
            data = form.cleaned_data['data']
            observacao = form.cleaned_data['observacao']
            imoveis = form.cleaned_data['imoveis']


            Despesas.objects.create(tipo=tipo, valor=valor, data=data, observacao=observacao, imoveis=imoveis,
                                    userid=request.user.id)
            return redirect('despesas_list')
        form.fields['imoveis'] = geeks_field
        return render(request, 'despesas/despesas_form.html', {'despesa':form})

# pia só brinquei aqui, pode alterar se quiser.
@login_required
def despesas_list(request):
    despesa = Despesas.objects.filter(userid=request.user.id)
    return render(request, 'despesas/despesas_list.html', {'despesa': despesa})


# se vc quiser criar aqui o calculo dos valore de despesas, vc pode usar essa função como exemplo
# Coloquei o mesmo calculo na app de relatorios, se quiser centralizar lá os relatorios.
# acho que essa função já te ajuda, no caso do Gregory, ele criou no models. Acho que aqui ou em relatorios
# já faz o calculo correto.

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