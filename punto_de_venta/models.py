#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from opciones import *


class Estados(models.Model):
	nombre=models.CharField(max_length=30)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Municipio(models.Model):
	estado=models.ForeignKey(Estados,on_delete=models.CASCADE)
	nombre=models.CharField(max_length=30)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Marca(models.Model):
	nombre=models.CharField(max_length=100)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Ubicacion(models.Model):
	calle=models.CharField(max_length=100)
	no_ext=models.CharField(max_length=10)
	no_int=models.CharField(max_length=10,null=True,blank=True)
	colonia=models.CharField(max_length=100)
	estado=models.ForeignKey(Estados)
	municipio=models.ForeignKey(Municipio)
	def __str__(self):
		if(self.no_int != None):
			return (self.calle+" #"+self.no_ext+" int. "+self.no_int+" Col. "+self.colonia+" "+self.municipio.nombre+","+self.estado.nombre).encode('utf-8')
		else:
			return (self.calle+" #"+self.no_ext+" Col. "+self.colonia+" "+self.municipio.nombre+","+self.estado.nombre).encode('utf-8')


class Contacto(models.Model):
	tel=models.CharField(max_length=10)
	cel=models.CharField(max_length=10)
	email=models.EmailField()
	facebook=models.CharField(max_length=10)
	def __str__(self):
		return ("tel. "+self.tel+" cel. "+self.cel+" email: "+self.email+" Facebook: "+self.facebook).encode('utf-8')

class Clientes(models.Model):
	clave=models.CharField(max_length=10)
	rfc=models.CharField(max_length=13)
	nombre=models.CharField(max_length=100)
	ubicacion=models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
	contacto=models.ForeignKey(Contacto,on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Proveedores(models.Model):
	clave=models.CharField(max_length=10)
	rfc=models.CharField(max_length=13)
	nombre=models.CharField(max_length=100)
	ubicacion=models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
	contacto=models.ForeignKey(Contacto,on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Medidas(models.Model):
	nombre=models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

class Departamento(models.Model):
	nombre=models.CharField(max_length=100)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Productos(models.Model):
	codigo_barras=models.CharField(max_length=100)
	sku=models.CharField(max_length=100)
	nombre=models.CharField(max_length=100)
	iva=models.IntegerField(choices=opcion_ivas)
	marca=models.ForeignKey(Marca)
	precio=models.DecimalField(max_digits=8,decimal_places=2)
	existencia=models.DecimalField(max_digits=8,decimal_places=2)
	proveedores=models.ManyToManyField(Proveedores)
	medida=models.ForeignKey(Medidas)
	dpto=models.ManyToManyField(Departamento)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Ventas(models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	cliente=models.ForeignKey(Clientes)
	total=models.DecimalField(max_digits=6,decimal_places=2)
	forma_pago=models.CharField(max_length=1,choices=opcion_forma_pago)
	monto=models.DecimalField(max_digits=6,decimal_places=2)
	cambio=models.DecimalField(max_digits=6,decimal_places=2)
	vendedor=models.ForeignKey('auth.User')
	iva_total=models.DecimalField(max_digits=6,decimal_places=2)
	subtotal=models.DecimalField(max_digits=6,decimal_places=2)
	
class Cajas(models.Model):
	descripcion=models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion.encode('utf-8')

class Caja_operacion(models.Model):
	fecha_inicio=models.DateTimeField(auto_now_add=True)
	vendedor=models.ForeignKey('auth.User')
	saldo_inicial=models.DecimalField(max_digits=6,decimal_places=2)
	saldo_final=models.DecimalField(max_digits=6,decimal_places=2)
	fecha_cierre=models.DateTimeField(auto_now_add=True)

class Detalle_Venta(models.Model):
	producto=models.ForeignKey(Productos)
	cantidad=models.DecimalField(max_digits=6,decimal_places=2)
	porcentaje_descuento=models.IntegerField(default=0)
	descuento=models.DecimalField(max_digits=6,decimal_places=2)
	venta=models.ForeignKey(Ventas)
	iva=models.DecimalField(max_digits=6,decimal_places=2)
