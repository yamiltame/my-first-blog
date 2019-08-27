from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^people$', views.person_list, name='person_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^person/$',views.make_person,name='person'),
    url(r'^person/(?P<pk>\d+)/$',views.person_detail,name='person_detail'),
    url(r'^test/$',views.test,name='test'),
    url(r'^test/calcular/(?P<nombre>.*)/(?P<fecha>.*)$',views.calcular,name='calcular'),
]
