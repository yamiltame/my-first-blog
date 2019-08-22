from django.conf.urls import url
from . import views

urlpatterns = [
    url('uno', views.post_list, name='post_list'),
    url('', views.post_2, name='post_2'),
]
