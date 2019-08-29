
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
	]
