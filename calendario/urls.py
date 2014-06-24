from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	#Admin
    url(r'^admin/', include(admin.site.urls)),
    
    #Inicio
    url(r'^', include('apps.inicio.urls')),
    
    #Eventos
    url(r'^evento/', include('apps.entidades.urls')),
   
    #login
    url(r'^', include('apps.logueo.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

)
