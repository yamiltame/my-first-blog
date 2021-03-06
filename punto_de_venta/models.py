#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from .validators import *
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
	no_ext=models.CharField(max_length=10,validators=[validate_digit])
	no_int=models.CharField(max_length=10,null=True,blank=True,validators=[validate_digit])
	colonia=models.CharField(max_length=100)
	estado=models.ForeignKey(Estados)
	municipio=models.ForeignKey(Municipio)
	codigo_postal=models.CharField(max_length=5,default=00000)
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
	precio=models.DecimalField(max_digits=8,decimal_places=2,validators=[validate_positive])
	existencia=models.DecimalField(max_digits=8,decimal_places=2,validators=[validate_positive])
	proveedores=models.ManyToManyField(Proveedores)
	medida=models.ForeignKey(Medidas)
	dpto=models.ManyToManyField(Departamento)
	def __str__(self):
		return self.nombre.encode('utf-8')

class Ventas(models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	cliente=models.ForeignKey(Clientes)
	total=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_positive])
	forma_pago=models.CharField(max_length=1,choices=opcion_forma_pago)
	monto=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_positive])
	cambio=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_positive])
	vendedor=models.ForeignKey('auth.User')
	iva_total=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_positive])
	subtotal=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_positive])
	caja=models.ForeignKey('Cajas',default=1)
	def __str__(self):
		return (self.vendedor.username+" caja: "+self.caja.descripcion+" "+self.fecha.strftime('%Y-%m-%d')+" "+self.total).encode('utf-8')

	
class Cajas(models.Model):
	descripcion=models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion.encode('utf-8')

class Caja_operacion(models.Model):
	caja=models.ForeignKey(Cajas)
	fecha_inicio=models.DateTimeField(auto_now_add=True)
	vendedor=models.ForeignKey('auth.User')
	saldo_inicial=models.DecimalField(max_digits=6,decimal_places=2)
	saldo_final=models.DecimalField(max_digits=6,decimal_places=2)
	fecha_cierre=models.DateTimeField(auto_now_add=False,null=True,blank=True)
	def __str__(self):
		fecha_cierre=self.fecha_cierre.strftime('%Y-%m-%d %H:%M')	if (self.fecha_cierre) else 'abierta'
		return "%s - %s - %s" % (self.caja.descripcion, self.fecha_inicio.strftime('%Y-%m-%d %H:%M'), fecha_cierre)

class Detalle_Venta(models.Model):
	producto=models.ForeignKey(Productos)
	cantidad=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_positive])
	porcentaje_descuento=models.IntegerField(default=0,validators=[validate_porcentaje])
	descuento=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_porcentaje])
	venta=models.ForeignKey(Ventas)
	iva=models.DecimalField(max_digits=6,decimal_places=2,validators=[validate_porcentaje])
	def __str__(self):
		return (self.producto.nombre+" cant: "+self.cantidad).encode('utf-8')
