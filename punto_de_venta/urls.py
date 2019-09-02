
from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.Inicio,name='inicio'),
	url(r'^agregarhumano/(?P<tipo>.*)/$',views.agregarhumano,name='agregarhumano'),
	url(r'^agregar/(?P<tipo>.*)/$',views.agregar,name='agregar'),
	url(r'^catalogo/(?P<tipo>.*)/$',views.catalogo,name='catalogo'),
	url(r'^editarhumano/(?P<tipo>.*)/(?P<pk>\d+)/$',views.editarhumano,name='editarhumano'),
	url(r'^editar/(?P<tipo>.*)/(?P<pk>\d+)/$',views.editar,name='editar'),
	url(r'^eliminar/(?P<tipo>.*)/(?P<pk>\d+)/$',views.eliminar,name='eliminar'),
	url(r'^ajax/cargarmunicipios/',views.cargarmunicipios,name='ajax_cargarmunicipios'),
	url(r'^ajax/cargarmarcas/',views.cargarmarcas,name='ajax_cargarmarcas'),
	url(r'^ajax/cargarmedidas/',views.cargarmedidas,name='ajax_cargarmedidas'),
	url(r'^ajax/cargardepartamento/',views.cargardepartamento,name='ajax_cargardepartamento'),
	url(r'^ejemplo/$',views.ejemplo,name='ejemplo'),
	url(r'^compra/(?P<pk>\d+)/$',views.compra,name='compra'),
	]
