from django import forms
from django.forms import ModelForm
from .models import LugarForm


class EventoForm(LugarForm):
	nombre_Evento = forms.CharField(max_length=50)
	descripcion = forms.CharField(widget=forms.Textarea)
	fecha = forms.CharField(max_length=50)
	propietario = forms.IntegerField()
