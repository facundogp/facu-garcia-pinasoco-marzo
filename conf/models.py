# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class Factura(models.Model):
    factura = models.IntegerField(max_length=50)
    cliente = models.ForeignKey(Cliente)


class Producto(models.Model):
    comida = models.CharField(max_length=50)
    cantidad = models.IntegerField(max_length=50)
    #fecha_compra = models.DateField(max_length=50)
    factura = models.ForeignKey(Factura)
