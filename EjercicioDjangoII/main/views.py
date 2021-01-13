#encoding:utf-8
from main.models import Album
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import urllib.request
import lxml
from datetime import datetime

#función auxiliar que hace scraping en la web y carga los datos en la base datos
def populateDB():
    #variables para contar el número de registros que vamos a almacenar
    num_albumes = 0
    
    #borramos todas las tablas de la BD
    Album.objects.all().delete()
    
    #extraemos los datos de la web con BS
    f = urllib.request.urlopen("https://www.elportaldemusica.es/lists/top-100-albums/2020/53")
    s = BeautifulSoup(f, "lxml")
    lista_albumes = s.find("div", class_="list-view").find_all("a")
    for link_album in lista_albumes:
        f = urllib.request.urlopen("https://www.elportaldemusica.es"+link_album.get('href'))
        s = BeautifulSoup(f, "lxml")
        datos = s.find("div", class_="container-fluid text-center").div
        ranking = datos.find("div", class_="publication_relevant").find("p", class_="single-list-entry-rank-position").string
        titulo = datos.find("div", class_="name").string
        autor = datos.find("div", class_="subname").find("a", class_="external").string
        semanas_en_lista = datos.find("div",class_="list_week").string
        maxPosicion = datos.find("div", class_="max_pos").string
        discografica = datos.find("div", class_="detail_one").string
        premios = datos.find("span", class_="number").string
        
        #almacenamos en la BD
        a = Album.objects.create(titulo = titulo, ranking = ranking,
                                autor = autor,
                                semanas = semanas_en_lista,                               
                                max_posicion = maxPosicion,
                                discografica = discografica,
                                premios = premios)
        #añadimos la lista de géneros
        num_albumes = num_albumes + 1

    return ((num_albumes))
        
#carga los datos desde la web en la BD
def carga(request):
 
    if request.method=='POST':
        if 'Aceptar' in request.POST:      
            num_albumes = populateDB()
            mensaje = "Se han almacenado: " + str(num_albumes) +" albumes" 
            return render(request, 'cargaBD.html', {'mensaje':mensaje})
        else:
            return redirect("/")
           
    return render(request, 'confirmacion.html')

#muestra el número de albumes que hay en la BD
def inicio(request):
    num_albumes=Album.objects.all().count()
    return render(request,'inicio.html', {'num_albumes':num_albumes})

#muestra un listado con los datos de los álbumes (título, ranking, autor, semanas, máxima posición, discográfica y premios)
def lista_albumes(request):
    albumes=Album.objects.all()
    return render(request,'albumes.html', {'albumes':albumes})

#muestra la lista de películas agrupadas por paises
def lista_albumesporranking(request):
    albumes=Album.objects.all().order_by('ranking')
    return render(request,'albumesporranking.html', {'albumes':albumes})
