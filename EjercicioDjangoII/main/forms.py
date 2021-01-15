#encoding:utf-8
from django import forms
from main.models import Genero
from main.models import Autor
   
class BusquedaPorGeneroForm(forms.Form):
    lista=[(g.id,g.nombre) for g in Genero.objects.all()]
    genero = forms.ChoiceField(label="Seleccione el género", choices=lista)
    
class BusquedaPorFechaForm(forms.Form):
    fecha = forms.DateField(label="Fecha (Formato dd/mm/yyyy)", widget=forms.DateInput(format='%d/%m/%Y'), required=True)
    
class BusquedaPorAutorForm(forms.Form):
    lista=[(a.id,a.nombre) for a in Autor.objects.all()]
    autor = forms.ChoiceField(label="Seleccione el autor", choices=lista)