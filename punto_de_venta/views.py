# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import *
from forms import *
from .tools import *
from django.http import HttpResponse

def Inicio(request):
	productos=get_catalogo('producto')
	clientes=get_catalogo('cliente')
	return render(request,'punto_de_venta/inicio.html',{'productos': productos,'clientes':clientes})

def agregar(request,tipo):
	if request.method == "POST":
		form=get_Fp(tipo,request)
		if form.is_valid():
			form.save()
			return redirect('catalogo',tipo=tipo)
	else:
		form=get_F(tipo)
	return render(request,'punto_de_venta/agregar.html',{'form':form,'tipo':tipo})

def agregarproducto(request):
	if request.method == "POST":
		form=get_Fp('producto',request)
		if form.is_valid():
			form.save()
			return redirect('catalogo',tipo='producto')
	else:
		form=get_F('producto')
	return render(request,'punto_de_venta/agregarproducto.html',{'form':form})

def agregarhumano(request,tipo):
	if request.method=='POST':
		form1=UbicacionForm(request.POST)
		form2=ContactoForm(request.POST)
		form3=get_Fp(tipo,request)
		if form1.is_valid() and form2.is_valid() and form3.is_valid():
			ubicacion=form1.save()
			contacto=form2.save()
			humano=form3.save(commit=False)
			humano.ubicacion =  ubicacion
			humano.contacto =  contacto
			humano.save()
			return redirect('catalogo', tipo=tipo)
	else:
		form1=UbicacionForm()
		form2=ContactoForm()
		form3=get_F(tipo)
	return render(request,'punto_de_venta/humanos.html',{'ubicacion':form1,'contacto':form2,'humano':form3,'tipo':tipo})

def catalogo(request,tipo):
	qs=get_catalogo(tipo)
	queryset=qs.order_by('nombre')
	return render(request,'punto_de_venta/catalogo.html',{'lista':queryset,'tipo':tipo})

def eliminar(request,pk,tipo):
	qs=get_E(tipo,pk)
	qs.delete()
	return redirect('catalogo',tipo=tipo)

def editar(request,tipo,pk):
	qs=get_E(tipo,pk)
	if request.method=='POST':
		form=get_Fe(tipo,request,qs)
		if form.is_valid():
			form.save()
			return redirect('catalogo', tipo=tipo)
	else:
		form=get_Fi(tipo,qs)
	return render(request,'punto_de_venta/agregar.html',{'form':form})

def editarhumano(request,tipo,pk):
	humano=get_E(tipo,pk)
	ubicacion=get_E('ubicacion',humano.ubicacion.pk)
	contacto=get_E('contacto',humano.contacto.pk)
	if request.method=='POST':
		form1=get_Fe(tipo,request,humano)
		form2=get_Fe('ubicacion',request,ubicacion)
		form3=get_Fe('contacto',request,contacto)
		if form1.is_valid() and form2.is_valid() and form2.is_valid():
			ubi=form2.save()
			cont=form3.save()
			hmn=form1.save(commit=False)
			hmn.ubicacion=ubi
			hmn.contacto=cont
			hmn.save()
			return redirect('catalogo', tipo=tipo)
	else:
		form1=get_Fi(tipo,humano)
		form2=get_Fi('ubicacion',ubicacion)
		form3=get_Fi('contacto',contacto)
	return render(request,'punto_de_venta/humanos.html',{'humano':form1, 'ubicacion':form2, 'contacto':form3, 'tipo':tipo })

def compra(request,pk):
	productos=Productos.objects.all()
	return render(request,'punto_de_venta/compra.html',{'productos':productos})

def cargarmunicipios(request):
	estado_id=request.GET.get('estado')
	municipios=Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
	return render(request,'punto_de_venta/municipios.html',{'municipios':municipios})

def cargarelemento(request,tipo):
	form=get_F(tipo)
	return render(request,'punto_de_venta/marcas.html',{'form':form,'tipo':tipo})

def cargarhumano(request,tipo):
	if request.method=='POST':
		form1=UbicacionForm(request.POST)
		form2=ContactoForm(request.POST)
		form3=get_Fp(tipo,request)
		if form1.is_valid() and form2.is_valid() and form3.is_valid():
			ubicacion=form1.save()
			contacto=form2.save()
			humano=form3.save(commit=False)
			humano.ubicacion =  ubicacion
			humano.contacto =  contacto
			humano.save()
			return redirect('catalogo', tipo=tipo)
	else:
		form1=UbicacionForm()
		form2=ContactoForm()
		form3=get_F(tipo)
	return render(request,'punto_de_venta/loadhumanos.html',{'ubicacion':form1,'contacto':form2,'humano':form3,'tipo':tipo})


def ajaxnuevo(request,tipo):
	form=get_Fp(tipo,request)
	elemento=form.save()
	diccionario[tipo][tipo]=elemento
	Form=parcialproducto(tipo,diccionario[tipo])
	return render(request,'punto_de_venta/regresoselect.html',{'form':Form})

def ajaxnuevohumano(request,tipo):
	form1=get_Fp(tipo,request)
	form2=get_Fp('ubicacion',request)
	form3=get_Fp('contacto',request)
	if form1.is_valid() and form2.is_valid() and form3.is_valid():
		elemento=form1.save(commit=False)
		ubicacion=form2.save()
		contacto=form3.save()
		elemento.ubicacion=ubicacion
		elemento.contacto=contacto
		elemento.save()
	Form=parcialproducto(tipo,{'elemento':elemento})
	print Form
	return render(request,'punto_de_venta/regresoselect.html',{'form':Form})

def ajaxregreso(request,tipo):
	form=parcialproducto(tipo,diccionario[tipo])
	print form
	return render(request,'punto_de_venta/regresoselect.html',{'form':form})

def ajaxdatoscliente(request,pk):
	cliente=Clientes.objects.get(pk=pk)
	return render(request,'punto_de_venta/loaddatoscliente.html',{'cliente':cliente})

def ajaxdatosproducto(request,pk):
	producto=Productos.objects.get(pk=pk)
	preciopublico=producto.precio*(producto.iva/100 +1)
	return render(request,'punto_de_venta/loaddatosproducto.html',{'producto':producto,'preciopublico':preciopublico})