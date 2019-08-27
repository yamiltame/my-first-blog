from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^marcas/$',views.nueva_marca,name='marcas'),
	url(r'^marcas/lista/$',views.lista_marcas,name='lista_marcas'),
	url(r'^marcas/editar/(?P<pk>\d+)/$',views.lista_marcas,name='marca_edit'),
	url(r'^marcas/eliminar/(?P<pk>\d+)/$',views.marca_eliminar,name='marca_eliminar'),
	]
