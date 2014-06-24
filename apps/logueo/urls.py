from django.conf.urls import patterns, include, url
from .views import index, inicio

urlpatterns = patterns('',
	url(r'^login/$', index.as_view()),
	url(r'^login/inicio$', inicio.as_view()),	
)
