from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='public/index.html'), name='home'),
	url(r'^loginerro/', TemplateView.as_view(template_name='erroLogin.html'), name='erro1'),
	url(r'^funcionario/', include('area_funcionario.urls')),
	url(r'^auth/', include('login.urls')),
	url(r'^cliente/', include('area_cliente.urls')),
    url(r'^admin/', admin.site.urls),
]