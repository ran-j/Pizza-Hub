#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from django.shortcuts import render
from models import Cadastropedido
from .forms import PedidoPizza,PesquisarPedido

def Index(request):
	return render(request, 'users/index.html')
	
	
def FazerPedido(request):
    if request.method == 'POST':
	form = PedidoPizza(request.POST)
	pDict = request.POST.copy() 
	form = PedidoPizza(pDict)
       
        if form.is_valid():
            sabo = form.cleaned_data.get('sabor')
            qtd = form.cleaned_data.get('quantidade')
            ender = form.cleaned_data.get('endereco')
            tel = form.cleaned_data.get('telefone')
            form = PedidoPizza()
            try:
	        numerodopedido = str(random.randint(10000, 99999))
				
                Cadastropedido.objects.create(sabor=sabo,quantidade=qtd,endereco=ender,telefone=tel,numerodepedido=numerodopedido)
                return render(request,'users/fazerfedido.html', {'form': form, 'reto': 'Pedido registrado com sucesso, número do pedido '+str(numerodopedido)})
		return http.HttpResponseRedirect('/cliente/pedidosconsulta/')
            except:
                return render(request,'users/fazerfedido.html',{'form': form, 'reto': 'Erro ao registrar pedido'})
    else:
        form = PedidoPizza()
    return render(request,'users/fazerfedido.html', {'form': form})
	
	
def Pedidos(request):
	if request.method == 'POST':
	
		form = PesquisarPedido(request.POST)
		pDict = request.POST.copy() 
		form= PesquisarPedido(pDict)
			
		if form.is_valid():
			numpedido = form.cleaned_data.get('numpedido')
			try:
				pedido = Cadastropedido.objects.get(numerodepedido=numpedido)
				return render(request,'users/mpedido.html',{'ped':pedido})
			except:
				form = PesquisarPedido()
				return render(request,'users/pedidos.html',{'form': form, 'reto':'Pedido não encontrado'})
	
	else:
		pedidoid = request.GET.get('ndepedido')
	
	if not pedidoid:
		form = PesquisarPedido()
		return render(request, 'users/pedidos.html',{'form': form})
	else:
		try:
			pedido = Cadastropedido.objects.get(numerodepedido=pedidoid)
			return render(request,'users/mpedido.html',{'ped':pedido})
		except:
			form = PesquisarPedido()
			return render(request,'users/pedidos.html',{'form': form, 'reto':'Pedido não encontrado'})
				
	form = PesquisarPedido()
	return render(request, 'users/pedidos.html',{'form': form})

	
