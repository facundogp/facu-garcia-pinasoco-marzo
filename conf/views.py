# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render

def registro(request):
    cliente = Cliente.objects.all()
    print cliente

    return render(request, 'registro.html', {'clientes_nombres':cliente})

def facturitas(request, id_cliente):
    cliente = Cliente.objects.get(id= id_cliente)
    print cliente
    factura = Factura.objects.filter(cliente = cliente)


    return render(request, 'facturitas.html', {'clientes_id':cliente, 'facturakey':factura})

def productito(request, id_factura):
    factura = Factura.objects.get(id= id_factura)
    print factura
    producto = Producto.objects.filter(factura = factura)

    return render(request, 'productito.html', {'factura_id':factura, 'productokey':producto})
