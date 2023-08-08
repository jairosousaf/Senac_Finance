from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from perfil.models import Conta

# Create your views here.

def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    contas = Conta.objects.all()
    total_contas = 0
    
    for conta in contas:
        total_contas += conta.valor
    
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas})

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
        
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar')
    
    conta = Conta(
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone
    )
    
    conta.save()
    messages.add_message(request, constants.SUCCESS, 'Cadastro feito com sucesso!')
    return redirect('/perfil/gerenciar')