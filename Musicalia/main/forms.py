#encoding:utf-8
from django import forms
from main.models import Autor
from main.models import Semanas 
       
class BusquedaPorAutorForm(forms.Form):
    lista=[(a.id,a.nombre) for a in Autor.objects.all()]
    autor = forms.ChoiceField(label="Seleccione el autor", choices=lista)
    
class BusquedaPorSemanasForm(forms.Form):
    lista=[(s.id,s.nombre) for s in Semanas.objects.all()]
    semanas = forms.ChoiceField(label="Seleccione las semanas", choices=lista)