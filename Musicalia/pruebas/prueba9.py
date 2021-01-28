#!/usr/bin/env python
# coding: utf-8

# In[1]:


#encoding:utf-8

from bs4 import BeautifulSoup
import urllib.request
from tkinter import *
from tkinter import messagebox
import sqlite3
import lxml
from datetime import datetime


# In[ ]:
## https://www.elportaldemusica.es/lists/top-100-albums/2020/53






# def recibir_datos():
#     f = urllib.request.urlopen("https://entradas.correos.es/categoria/conciertos-98?page=1")
#     s = BeautifulSoup(f, "lxml")
#     lista_albumes = s.find("div", class_="package-list-item-wrapper on-page-result-page").find("h4", class_="mb-0").find_all("a")
#     for link_album in lista_albumes:
#         print(link_album)
#         f = urllib.request.urlopen("https://entradas.correos.es"+link_album.a['href'])  
#         s = BeautifulSoup(f, "lxml")
#         datos = s.find("div", class_="main-wrapper")
#         concierto = datos.find("div", class_="flex-column flex-md-8 flex-sm-12").find("h1", class_="hero-title").string
#         print(concierto)
#         lugar = datos.find("div", class_="raty-wrapper").find("span", style="display: block;").string
# def extraer_concierto():
#     lista_concierto = []
#         
#     for i in range(1, 4):
#         lista_pagina = recibir_datos("https://www.eventbrite.es/d/spain/music--events/?page=" + str(i))
#         lista_concierto.extend(lista_pagina)
#     return lista_concierto
# 
# def recibir_datos(url):
#     lista = []
#     f = urllib.request.urlopen(url)
#     s = BeautifulSoup(f, "lxml")
#     lista_albumes = s.find("ul", class_="search-main-content__events-list").find_all("li")
#     for link_album in lista_albumes:
#         
#         #href="https://www.eventbrite.es/e/entradas-de-regreso-a-los-80s-sesion-especial-sabado-30-enero-136584109749?aff=ebdssbdestsearch"
#         f = urllib.request.urlopen(link_album.a['href'])
#         s = BeautifulSoup(f, "lxml")
#         concierto = s.find("h1", class_="listing-hero-title").string
#         dia = s.find("p", class_="js-date-time-first-line").string
#         precio = s.find("div", class_="js-display-price").string
#         lista.append((concierto, dia, precio))
#     return lista
#         
#         
# 
# 
# # In[3]:
# 
# 
# extraer_concierto()


# In[ ]:

# def almacenar_datos():
#    
#     #extraemos los datos de la web con BS
#     f = urllib.request.urlopen("https://www.elportaldemusica.es/lists/top-100-albums/2020/53")
#     s = BeautifulSoup(f, "lxml")
#     lista_albumes = s.find("div", class_="list-view").find_all("a")
#     lista = []
#     for link_album in lista_albumes:
#         f = urllib.request.urlopen("https://www.elportaldemusica.es"+link_album.get('href'))
#         s = BeautifulSoup(f, "lxml")
#         datos = s.find("div", class_="container-fluid text-center").div
# 
#         titulo = datos.find("div", class_="name").string
#         autor = datos.find("div", class_="subname").find("a", class_="external").string
# 
# 
#         lista.append((titulo, autor))
# 
#     return lista
# 
# def cargar_whoosh():
#     
#     # define el esquema de la informaciÃ³n
#     schem = Schema(titulo=TEXT(stored=True), autor=TEXT(stored=True))
#     
#     # eliminamos el directorio del Ã­ndice, si existe
#     if os.path.exists("Index"):
#         shutil.rmtree("Index")
#     os.mkdir("Index")
#     
#     # creamos el Ã­ndice
#     ix = create_in("Index", schema=schem)
#     # creamos un writer para poder aÃ±adir documentos al indice
#     writer = ix.writer()
#     i = 0
#     lista = almacenar_datos()
#     for album in lista:
#         writer.add_document(titulo=str(album[0]), autor=str(album[1]))    
#         i += 1
#     writer.commit()
#     
# 
# def mostrar_titulo_autor(request):
# 
#     ix = open_dir("Index")
#     with ix.searcher() as searcher:
#             results = searcher.all_stored_fields()
#             lista = []
#             for r in results:
#                 titulo = r['titulo']
#                 autor = r['autor']
#                 lista.append((titulo,autor))
#     return render(request, 'carga_whoohs.html', {'lista':lista})




