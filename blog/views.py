# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

def post_list(request):
#	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts=Post.objects.all().order_by('published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
	post=Post.objects.get(pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})