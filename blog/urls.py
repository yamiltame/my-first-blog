from django.conf.urls import url
from . import views

urlpatterns = [
    url('uno', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
#    url('post/<int:pk>/', views.post_detail, name='post_detail'),
]