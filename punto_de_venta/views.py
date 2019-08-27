# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Clientes
from .models import Marca
from forms import MarcaForm
from django.shortcuts import redirect


def punto_venta(request):
	return render(request,'punto_de_venta')

def lista_marcas(request):
	marcas=Marca.objects.all()
	return render(request,'punto_de_venta/lista_marcas.html',{'marcas':marcas})

def nueva_marca(request):
	if request.method == "POST":
		form=MarcaForm(request.POST)
		if form.is_valid():
			marca=form.save(commit=False)
			marca.save()
			return redirect('lista_marcas')
	else:
		form=MarcaForm()
	return render(request,'punto_de_venta/marcas.html',{'form':form})

def marca_eliminar(request,pk):
	marca=Marca.objects.get(pk=pk)
	marca.delete()
	return redirect('lista_marcas')

