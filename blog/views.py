# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Person 
from django.contrib.auth.models import User
from .forms import PostForm
from .forms import PersonForm
from .forms import user
from django.shortcuts import redirect
from datetime import date

# Create your views here.

def post_list(request):
#	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts=Post.objects.all().order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def person_list(request):
	people=Person.objects.all()
	return render(request,'blog/person_list.html',{'people':people})

def post_detail(request, pk):
	post=Post.objects.get(pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})

def person_detail(request,pk):
	person=Person.objects.get(pk=pk)
	return render(request,'blog/person_detail.html',{'person':person})

def post_new(request):
	if request.method == "POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form=PostForm()
	return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
	post=get_object_or_404(Post,pk=pk)
	if request.method == "POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'blog/post_edit.html', {'form': form})

def make_person(request):
	if request.method == "POST":
		form=PersonForm(request.POST)
		if form.is_valid():
			person=form.save(commit=False)
			person.save()
			return redirect('person_detail',pk=person.pk)
	else:
		form=PersonForm()
	return render(request,'blog/addperson.html',{'form':form})

def test(request):
	if request.method=='POST':
		form=user(request.POST)
		if form.is_valid():
			nombre=form.cleaned_data['nombre']
			fecha=form.cleaned_data['fecha_nacimiento']
			print nombre
			print fecha
			return redirect('calcular',nombre=nombre,fecha=fecha)
	else:
		form=user()
	return render(request,'blog/test.html',{'form':form})

def calcular(request,nombre,fecha):
	dicc={'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
	agno=fecha[0:4]
	mes=fecha[5:7]
	dia=fecha[8:10]
	return render(request,'blog/calcular.html',{'agno':agno,'mes':dicc[mes],'dia':dia})



