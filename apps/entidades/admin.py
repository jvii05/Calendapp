from django.contrib import admin
from .models import Tarea,Lugar,NotaRapida,EventoSocial

admin.site.register(NotaRapida)
admin.site.register(Tarea)
admin.site.register(EventoSocial)
admin.site.register(Lugar)
