from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView
from apps.entidades.models import Tarea,EventoSocial
from django.contrib.auth.models import User

def index(request):
	return render_to_response('inicio/index.html')
	
class index2(ListView):
	template_name = 'inicio/index2.html'
	model = EventoSocial
	object_context_name = 'eventos'
	
	def get_context_data(self, **kwargs):
		context = super(index2, self).get_context_data(**kwargs)
		context['eventos_sociales'] = EventoSocial.objects.all()
		context['tareas'] = Tarea.objects.all()
		return context

