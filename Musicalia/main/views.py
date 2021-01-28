#encoding:utf-8
from main.forms import BusquedaPorAutorForm
from main.forms import BusquedaPorSemanasForm
from main.models import Album, Autor, Semanas
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import urllib.request
import lxml
from datetime import datetime
import re, os, shutil
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, DATETIME, KEYWORD
from whoosh.qparser import QueryParser, MultifieldParser, OrGroup

#función auxiliar que hace scraping en la web y carga los datos en la base datos
def populateDB():
    #variables para contar el número de registros que vamos a almacenar
    num_albumes = 0
    
    #borramos todas las tablas de la BD
    Album.objects.all().delete()
    Autor.objects.all().delete()
    Semanas.objects.all().delete()
    
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
        semanas= datos.find("div",class_="list_week").string
        maxPosicion = datos.find("div", class_="max_pos").string
        discografica = datos.find("div", class_="detail_one").string
        premios = datos.find("span", class_="number")
        if(premios == None):
            premios = 0
        else:
            premios = premios.string
        
        #almacenamos en la BD

        a = Album.objects.create(titulo = titulo, ranking = ranking,
                                max_posicion = maxPosicion,
                                discografica = discografica,
                                premios = premios)
        #añadimos el autor
        aut = Autor.objects.create(nombre=autor)
        a.autor.add(aut)
        
        #añadimos las semanas
        sem = Semanas.objects.create(nombre=semanas)
        a.semanas.add(sem)

        

        num_albumes = num_albumes + 1

    return ((num_albumes))
        
#carga los datos desde la web en la BD
def carga(request):
 
    if request.method=='POST':
        if 'Aceptar' in request.POST:      
            num_albumes = populateDB()
            cargar_whoosh()
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

def buscar_albumes_semanas(request):
    formulario = BusquedaPorSemanasForm()
    albumes = None
    
    if request.method=='POST':
        formulario = BusquedaPorSemanasForm(request.POST)      
        if formulario.is_valid():
            semanas=Semanas.objects.get(id=formulario.cleaned_data['semanas'])
            albumes = semanas.album_set.all()
            
    return render(request, 'albumes-busqueda-por-semanas.html', {'formulario':formulario, 'albumes':albumes})
    

        
def almacenar_datos():
   
    #extraemos los datos de la web con BS
    f = urllib.request.urlopen("https://www.elportaldemusica.es/lists/top-100-albums/2020/53")
    s = BeautifulSoup(f, "lxml")
    lista_albumes = s.find("div", class_="list-view").find_all("a")
    lista = []
    for link_album in lista_albumes:
        f = urllib.request.urlopen("https://www.elportaldemusica.es"+link_album.get('href'))
        s = BeautifulSoup(f, "lxml")
        datos = s.find("div", class_="container-fluid text-center").div

        titulo = datos.find("div", class_="name").string
        autor = datos.find("div", class_="subname").find("a", class_="external").string


        lista.append((titulo, autor))

    return lista

def cargar_whoosh():
    
    # define el esquema de la informaciÃ³n
    schem = Schema(titulo=TEXT(stored=True), autor=TEXT(stored=True))
    
    # eliminamos el directorio del Ã­ndice, si existe
    if os.path.exists("Index"):
        shutil.rmtree("Index")
    os.mkdir("Index")
    
    # creamos el Ã­ndice
    ix = create_in("Index", schema=schem)
    # creamos un writer para poder aÃ±adir documentos al indice
    writer = ix.writer()
    i = 0
    lista = almacenar_datos()
    for album in lista:
        writer.add_document(titulo=str(album[0]), autor=str(album[1]))    
        i += 1
    writer.commit()
    

def mostrar_titulo_autor(request):

    ix = open_dir("Index")
    with ix.searcher() as searcher:
            results = searcher.all_stored_fields()
            lista = []
            for r in results:
                titulo = r['titulo']
                autor = r['autor']
                lista.append((titulo,autor))
    return render(request, 'carga_whoohs.html', {'lista':lista})
    
