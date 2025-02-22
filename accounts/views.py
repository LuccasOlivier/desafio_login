from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


# View para a página de login
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if not email or not password:
            messages.error(request, 'E-mail e senha são obrigatórios.')
            return redirect('login')  # Retorna para a página de login

        user = authenticate(request, username=email, password=password)

        # Mensagens de erro personalizadas
        if not User.objects.filter(username=email).exists():
            messages.error(request, 'E-mail inexistente.')
        elif user is None:
            messages.error(request, 'Senha inválida.')
        else:
            login(request, user)
            return redirect('menu')

    # Se não for uma requisição POST, renderiza a página normalmente
    return render(request, 'login.html')


# View para a página de registro
def register_view(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        # Validação do nome (apenas letras)
        if not nome.isalpha():
            messages.error(request, 'O nome deve conter apenas letras.')
            return redirect('register')

        # Validação do e-mail
        if '@' not in email or '.' not in email:
            messages.error(request, 'E-mail inválido.')
            return redirect('register')

        # Validação da senha
        if (
            len(senha) < 8 or 
            not re.search(r'[A-Z]', senha) or 
            not re.search(r'[0-9]', senha) or 
            not re.search(r'[\W_]', senha)
        ):
            messages.error(request, 'A senha deve conter pelo menos 8 caracteres, 1 caractere especial, 1 número e 1 letra maiúscula.')
            return redirect('register')

        # Verifica se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('register')

        # Se todas as validações passaram
        user = User.objects.create_user(username=email, password=senha, first_name=nome)
        messages.success(request, 'Usuário registrado com sucesso!')
        return redirect('login')  # Após o registro, redireciona para a tela de login

    return render(request, 'register.html')

# View para a página do menu, acessível apenas para usuários logados
@login_required
def menu_view(request):
    return render(request, 'menu.html')

# View para realizar o logout
def logout_view(request):
    
    logout(request)
    
    # Limpar mensagens persistentes da sessão
    from django.contrib.messages import get_messages
    get_messages(request)  # limpar qualquer mensagem armazenada na sessão
    
    messages.info(request, 'Você foi deslogado com sucesso!')
    
    return redirect('login')  # Redireciona para a página de login