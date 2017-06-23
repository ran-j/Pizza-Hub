#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import CadastroMateriais
from area_cliente.models import Cadastropedido
from django.contrib.auth.decorators import login_required

from .forms import ItensForm
from area_cliente.forms import PesquisarPedido

@login_required(login_url='/loginerro')
def Index(request):
	return render(request, 'funci/index.html')
		

@login_required(login_url='/loginerro')
def Cadastroprodutos(request):
    if request.method == 'POST':
	form = ItensForm(request.POST)
	pDict = request.POST.copy() 
	form = ItensForm(pDict)
       
        if form.is_valid():
            nopro = form.cleaned_data.get('nomepro')
            qtd = form.cleaned_data.get('quantidade')
            precu = form.cleaned_data.get('precounitario')
            nf = form.cleaned_data.get('notafiscal')
            form = ItensForm()
            try:
                CadastroMateriais.objects.create(nome=nopro,quantidade=qtd, precounitario=precu, notafiscal=nf)
                return render(request, 'funci/cadastorpro.html', {'form': form, 'reto': 'Iten cadastrado'})
		return http.HttpResponseRedirect('/cadastroprodutos/')
            except:
                return render(request, 'funci/cadastorpro.html',{'form': form, 'reto': 'Erro ao cadastrar'})

    else:
        form = ItensForm()
    return render(request, 'funci/cadastorpro.html', {'form': form})
	
@login_required(login_url='/loginerro')
def Estoque(request):
    if request.method == 'GET':
        lista_itens = CadastroMateriais.objects.all()

    return render(request, 'funci/estoques.html', {'lista_itens': lista_itens})
	
@login_required(login_url='/loginerro')
def Pedidos(request):
	lista_pedidos = Cadastropedido.objects.all()
	return render(request,'funci/mpedido.html',{'ped':lista_pedidos})
