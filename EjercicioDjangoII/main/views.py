#encoding:utf-8
from main.forms import BusquedaPorAutorForm
from main.models import Album, Autor
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
    Autor.objects.all().delete()
    
    #extraemos los datos de la web con BS
    f = urllib.request.urlopen("https://www.elportaldemusica.es/lists/top-100-albums/2020/53")
    s = BeautifulSoup(f, "lxml")
    lista_albumes = s.find("div", class_="list-view").find_all("a")
    for link_album in lista_albumes:
        f = urllib.request.urlopen("https://www.elportaldemusica.es"+link_album.get('href'))
        s = BeautifulSoup(f, "lxml")
        datos = s.find("div", class_="container-fluid text-center").div
        ranking = datos.find("div", class_="publication_relevant").find("p", class_="single-list-entry-rank-position")
        if(ranking == None):
            ranking = 0
        else:
            ranking = ranking.string
        titulo = datos.find("div", class_="name").string
        autor = datos.find("div", class_="subname").find("a", class_="external").string
        semanas_en_lista = datos.find("div",class_="list_week").string
        maxPosicion = datos.find("div", class_="max_pos").string
        discografica = datos.find("div", class_="detail_one").string
        premios = datos.find("span", class_="number")
        if(premios == None):
            premios = 0
        else:
            premios = premios.string
        
        #almacenamos en la BD

        a = Album.objects.create(titulo = titulo, ranking = ranking,
                                semanas = semanas_en_lista,                               
                                max_posicion = maxPosicion,
                                discografica = discografica,
                                premios = premios)
        #añadimos el autor
        aut = Autor.objects.create(nombre=autor)
        a.autor.add(aut)


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

#muestra la lista de albumes agrupadas por ranking
def lista_album_ranking(request):
    albumes=Album.objects.all().order_by('ranking')
    return render(request,'album-por-ranking.html', {'albumes':albumes})

def lista_premios(request):
    albumes=Album.objects.all().order_by('ranking')
    return render(request,'album-por-ranking.html', {'albumes':albumes})


def buscar_albumes_autor(request):
    formulario = BusquedaPorAutorForm()
    albumes = None
    
    if request.method=='POST':
        formulario = BusquedaPorAutorForm(request.POST)      
        if formulario.is_valid():
            autor=Autor.objects.get(id=formulario.cleaned_data['autor'])
            albumes = autor.album_set.all()
            
    return render(request, 'albumes-busqueda-por-autor.html', {'formulario':formulario, 'albumes':albumes})
    
