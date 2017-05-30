from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register', views.criaruser, name='rgt'),
	url(r'^login', views.logina, name='lng'),
	url(r'^logout', views.sair, name='lgt'),
]
