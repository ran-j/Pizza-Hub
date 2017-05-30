from __future__ import unicode_literals

from django.db import models

class CadastroMateriais(models.Model):
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    precounitario = models.DecimalField(max_digits=7, decimal_places=2)
    notafiscal = models.IntegerField(default=0)
    