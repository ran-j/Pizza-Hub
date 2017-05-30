#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm

Sabores = (
    ('Calabresa', 'Calabresa'),
    ('Portuguesa', 'Portuguesa'),
    ('Mussarela', 'Mussarela'),
)


class PedidoPizza(forms.Form):
    sabor =  forms.CharField(widget=forms.Select(choices=Sabores))
    quantidade = forms.IntegerField(label='Quantidade',max_value=20)
    endereco = forms.CharField(label='Endereço', max_length=100)
    telefone = forms.IntegerField(label='Telefone')
	
	
class PesquisarPedido(forms.Form):
    numpedido = forms.IntegerField(label='Número do pedido')