#encoding:utf-8
from django import forms
from main.models import Genero
from main.models import Premio
   
class BusquedaPorGeneroForm(forms.Form):
    lista=[(g.id,g.nombre) for g in Genero.objects.all()]
    genero = forms.ChoiceField(label="Seleccione el género", choices=lista)
    
class BusquedaPorFechaForm(forms.Form):
    fecha = forms.DateField(label="Fecha (Formato dd/mm/yyyy)", widget=forms.DateInput(format='%d/%m/%Y'), required=True)
    
class BusquedaPorPremioForm(forms.Form):
    lista=[(p.id,p.nombre) for p in Premio.objects.all()]
    premios = forms.ChoiceField(label="Seleccione el premio", choices=lista)