# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Estados)
admin.site.register(Municipio)
admin.site.register(Proveedores)
admin.site.register(Contacto)
admin.site.register(Ubicacion)
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Ventas)
admin.site.register(Detalle_Venta)
admin.site.register(Caja_operacion)
admin.site.register(Cajas)
# Register your models here.
