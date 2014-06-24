from django.conf.urls import patterns, include, url
from .views import crearNotaRapida,crearTarea,registroExitoso,crearEvento

urlpatterns = patterns('',

    url(r'^nuevaNota/', crearNotaRapida.as_view(),name="nueva_nota"),
    
    url(r'^nuevaTarea/', crearTarea.as_view(),name="nueva_tarea"),
    
	url(r'^nuevoEvento/', crearEvento.as_view(),name="nuevo_evento"),
    
    url(r'^registroExito/', registroExitoso.as_view(),name="registro_exitoso"),
)
