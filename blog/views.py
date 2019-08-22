# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#urlpatterns = [
#    url('', views.post_list, name='post_list'),
#]

def post_list(request):
	return render(request,'blog/post_list.html',{})

def post_2(request):
	return render(request,'blog/post_2.html',{})