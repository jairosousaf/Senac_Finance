from perfil.models import Categoria, Conta
from django.contrib.messages import constants
from django.contrib import messages
from django.shortcuts import redirect, render
from extrato.models import Valores
from datetime import datetime

def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    elif request.method == "POST":
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')
       
        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )

        valores.save()

        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += int(valor)
        else:
            conta.valor -= int(valor)

        conta.save()        
        
        if tipo == 'E':
            messages.add_message(request, constants.SUCCESS, 'Entrada realizada com sucesso!')
        else:
            messages.add_message(request, constants.SUCCESS, 'Retirada realizada com sucesso!')
            
        return redirect('/extrato/novo_valor')

def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
       
    valores = Valores.objects.filter(data__month=datetime.now().month)
 
    return render(request, 'view_extrato.html', {'valores': valores, 'contas': contas, 'categorias': categorias})