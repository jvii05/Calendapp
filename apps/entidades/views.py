from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, FormView, ListView
from django.template import RequestContext
from .models import NotaRapida,Tarea,Lugar, LugarForm, EventoSocial
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.utils.timesince import timesince
from django.utils import simplejson
from django.shortcuts import render_to_response

from .forms import EventoForm 

class crearNotaRapida(CreateView):
	template_name = 'entidades/nuevaNotaRapida.html'
	model = NotaRapida
	success_url = reverse_lazy('registro_exitoso')
	
class crearTarea(CreateView):
	template_name = 'entidades/nuevaTarea.html'
	model = Tarea
	success_url = reverse_lazy('registro_exitoso')
	
class crearEvento(FormView):
	template_name = 'entidades/nuevoEvento.html'
	form_class = EventoForm
	success_url = reverse_lazy('registro_exitoso')

	def form_valid(self, form):
		lugar = form.save()
		propietario = self.request.user
		evento = EventoSocial()
		evento.lugar = lugar
		evento.nombre = form.cleaned_data['nombre_Evento']
		evento.descripcion = form.cleaned_data['descripcion']
		evento.fecha = form.cleaned_data['fecha']
		#Obtiene el usuario autentificado para colocarlo como propietario
		evento.propietario = User.objects.get(pk=form.cleaned_data['propietario'])
		evento.save()
		return super(crearEvento , self).form_valid(form)

class registroExitoso(TemplateView):
	template_name =  'entidades/registroExitoso.html'
	

	
	

	
'''
class agregarEvento(FormView):
	template_name = 'entidades/nuevoEvento.html'
	form_class = EventoForm
	success_url = reverse_lazy('registro_exitoso')
	
	def form_valid(self, form):
		lugar = form.save()
		return super(agregarEvento , self).form_valid(form)
	
def crearEvento(request):
	form = LugarForm()
	#ubicaciones = Lugar.objects.all()
	return render_to_response('entidades/nuevoEvento.html', 
					{ 'form':form},# 'ubicaciones': ubicaciones},
					context_instance = RequestContext(request))
					'''
						
def coords_save(request):
	if request.is_ajax():
		form = UbicacionForm(request.POST)
		if form.is_valid():
			form.save()
			
			return HttpResponse(simplejson.dumps({'ok': True, 'msg': data }), mimetype='application/json')
		else:
			return HttpResponse(simplejson.dumps({'ok':False, 'msg': 'Debes llenar los campos'}), mimetype='application/json')
	
