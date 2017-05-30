#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ItensForm(forms.Form):
    nomepro = forms.CharField(label='Nome do produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')
    precounitario = forms.DecimalField(label='Preço unitário',max_digits=5)
    notafiscal = forms.IntegerField(label='Nota Fiscal')
	