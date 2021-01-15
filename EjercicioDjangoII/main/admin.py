from django.contrib import admin
from main.models import Autor, Semanas, Album

#registramos en el administrador de django los modelos 

admin.site.register(Semanas)
admin.site.register(Autor)
admin.site.register(Album)