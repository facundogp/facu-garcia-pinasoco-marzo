# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin


admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Cliente)

# Register your models here.
