from .forms import formproprietario
from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from .models import proprietarios
from django.contrib.auth.models import User
from django.contrib import messages


def create_proprietario(request):
    create = formproprietario(request.POST or None)
   # print(create.is_valid)

    if create.is_valid():
        name = create.cleaned_data['nome']
        identidade = create.cleaned_data['identidade']
        cpf = create.cleaned_data['cpf']
        username = create.cleaned_data['username']
        password1 = create.cleaned_data['password']
        password2 = create.cleaned_data['password2']
        email = create.cleaned_data['email']
        cep = create.cleaned_data['cep']
        telefone = create.cleaned_data['telefone']
        endereco = create.cleaned_data['endereco']
        numero = create.cleaned_data['numero']
        bairro = create.cleaned_data['bairro']
        cidade = create.cleaned_data['cidade']
        estado = create.cleaned_data['estado']
        print('--------------------', estado)

        if password1 != password2:
            messages.error(request, 'A senha está divergente.!')
            return render(request, 'account/signup.html', {'create': create})

        else:
            ultimo_id = User.objects.create_user(username=username, email=email, password=password1).id
            #print('testando', ultimo_id)
            proprietarios.objects.create(nome=name, identidade=identidade, cpf=cpf, telefone=telefone,
                                         endereco=endereco, numero=numero, bairro=bairro, cidade=cidade,
                                         cep=cep, estado=estado,userid=ultimo_id)
            messages.success(request, 'cadastro efetuado com sucesso.!')

            return redirect('login')

    else:
        messages.error(request, 'Erro ao cadastrar.!')
    return render(request, 'proprietario/signup.html', {'create': create})




