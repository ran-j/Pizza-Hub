from django.conf.urls import include,url

from . import views

urlpatterns = [
	url(r'^cadastroprodutos/', views.Cadastroprodutos, name='cdprod'),
	url(r'^produtos/', views.Estoque, name='estq'),
	url(r'^pedidosfn/', views.Pedidos, name='pedi'),
	url(r'^logout', include('login.urls')),
	url(r'^', views.Index, name='iniaa'),
]
