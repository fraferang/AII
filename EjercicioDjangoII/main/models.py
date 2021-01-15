#encoding:utf-8
from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Género')

    def __str__(self):
        return self.nombre
    
class Director(models.Model):
    nombre = models.CharField(max_length=30,verbose_name='Director')

    def __str__(self):
        return self.nombre
    
class Pais(models.Model):
    nombre = models.CharField(max_length=30,verbose_name='País')

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.TextField(verbose_name='Título')
    tituloOriginal = models.TextField(verbose_name='Título Original')
    fechaEstreno = models.DateField(verbose_name='Fecha de Estreno')
    pais = models.ForeignKey(Pais,on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director,on_delete=models.SET_NULL, null=True)
    generos = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo



class Autor(models.Model):
    nombre = models.TextField(null=True,verbose_name='Autor')

    def __str__(self) -> str:
        return self.nombre
        
## Clase Álbum
class Album(models.Model):
    titulo = models.TextField(verbose_name='Título')
    ranking = models.IntegerField(null=True,max_length=20,verbose_name='Ranking actual')
    autor = models.ManyToManyField(Autor)
    semanas = models.TextField(verbose_name='Semanas en lista')
    max_posicion = models.TextField(verbose_name='Máxima posición alcanzada')
    discografica = models.TextField(verbose_name='Discográfica')
    premios = models.IntegerField(null=True,verbose_name='Premios')

    def __str__(self):
        return self.titulo
