
from django.conf.urls import url, include
from . import views

urlpatterns=[
	url(r'^$',views.Inicio,name='inicio'),
	url(r'^agregarhumano/(?P<tipo>.*)/$',views.agregarhumano,name='agregarhumano'),
	url(r'^agregarproducto/$',views.agregarproducto,name='agregarproducto'),
	url(r'^agregarproductomultiple/$',views.agregarproductomultiple,name='agregarproductomultiple'),
	url(r'^agregar/(?P<tipo>.*)/$',views.agregar,name='agregar'),
	url(r'^catalogo/(?P<tipo>.*)/$',views.catalogo,name='catalogo'),
	url(r'^editarhumano/(?P<tipo>.*)/(?P<pk>\d+)/$',views.editarhumano,name='editarhumano'),
	url(r'^editar/(?P<tipo>.*)/(?P<pk>\d+)/$',views.editar,name='editar'),
	url(r'^eliminar/(?P<tipo>.*)/(?P<pk>\d+)/$',views.eliminar,name='eliminar'),
	url(r'^ajax/cargarmunicipios/',views.cargarmunicipios,name='ajax_cargarmunicipios'),
	url(r'^ajax/cargar/(?P<tipo>\w+)/$',views.cargarelemento,name='ajax_cargarelemento'),
	url(r'^ajax/cargarhumano/(?P<tipo>\w+)/$',views.cargarhumano,name='ajax_cargarproveedor'),
	url(r'^ajax/nuevo/(?P<tipo>\w+)/$',views.ajaxnuevo,name='ajaxnuevo'),
	url(r'^ajax/nuevohumano/(?P<tipo>\w+)/$',views.ajaxnuevohumano,name='ajaxnuevohumano'),
	url(r'^ajax/regreso/(?P<tipo>\w+)/$',views.ajaxregreso,name='ajaxregreso'),
	url(r'^ajax/getdatoscliente/(?P<pk>\d+)/$',views.ajaxdatoscliente,name='ajaxdatoscliente'),
	url(r'^ajax/getdatosproducto/(?P<pk>\d+)/$',views.ajaxdatosproducto,name='ajaxdatosproducto'),
	url(r'^ajax/datosreporte/$',views.ajaxdatosreporte,name='ajaxdatosreporte'),
	url(r'^ajax/makeformset/$',views.ajaxmakeformset,name='ajaxmakeformset'),
	url(r'^hacercompra/$',views.hacercompra,name='hacercompra'),
	url(r'^registro/$',views.SignUp.as_view(),name='registro'),
	url(r'^makelogin/$',views.makelogin,name='makelogin'),
	url(r'^makelogout/$',views.makelogout,name='makelogout'),
	url(r'^reportes/$',views.reportes,name='reportes'),
	]
