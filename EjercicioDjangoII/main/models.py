#encoding:utf-8
from django.db import models


class Autor(models.Model):
    nombre = models.TextField(null=True,verbose_name='Autor')

    def __str__(self) -> str:
        return self.nombre
    
class Semanas(models.Model):
    nombre = models.TextField(null=True,verbose_name='Semanas')

    def __str__(self) -> str:
        return self.nombre
        
## Clase Álbum
class Album(models.Model):
    titulo = models.TextField(verbose_name='Título')
    ranking = models.IntegerField(null=True,max_length=20,verbose_name='Ranking actual')
    autor = models.ManyToManyField(Autor)
    semanas = models.ManyToManyField(Semanas)
    max_posicion = models.TextField(verbose_name='Máxima posición alcanzada')
    discografica = models.TextField(verbose_name='Discográfica')
    premios = models.IntegerField(null=True,verbose_name='Premios')

    def __str__(self):
        return self.titulo
