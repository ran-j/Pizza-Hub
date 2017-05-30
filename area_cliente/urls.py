from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^fazerpedido/', views.FazerPedido, name='mpedido'),
	url(r'^pedidosconsulta/', views.Pedidos, name='mpedido'),
	url(r'^', views.Index, name='iniaa'),
]
