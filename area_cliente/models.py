from __future__ import unicode_literals

from django.db import models

class Cadastropedido(models.Model):

    sabor = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=1)
    endereco = models.CharField(max_length=200)
    telefone = models.IntegerField()
    numerodepedido = models.IntegerField(default=9999999, unique=True)
    status = models.CharField(max_length=200,default="Aguardando")
