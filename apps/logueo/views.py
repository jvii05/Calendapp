from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template.context import RequestContext

# Create your views here.

class index(TemplateView):	
	def get(self, request, *args, **kwargs):
		context = RequestContext(request,
                           {'request': request,
                           'user': request.user})
		return render_to_response('logueo/index.html', 
							context_instance = context)
							
class inicio(TemplateView):
	def get(self, request, *args, **kwargs):
		context = RequestContext(request,
                           {'request': request,
                           'user': request.user})
		return render_to_response('logueo/inicio.html', 
							context_instance = context)
