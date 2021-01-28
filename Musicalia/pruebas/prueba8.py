#!/usr/bin/env python
# coding: utf-8

# In[1]:

# 
# #encoding:utf-8
# 
# from bs4 import BeautifulSoup
# import urllib.request
# from tkinter import *
# from tkinter import messagebox
# import sqlite3
# import lxml
# from datetime import datetime
# from tkinter import *
# from tkinter import messagebox
# import re, os, shutil
# from whoosh.index import create_in, open_dir
# from whoosh.fields import Schema, TEXT, DATETIME, KEYWORD
# from whoosh.qparser import QueryParser, MultifieldParser, OrGroup
# 
# 
# # In[ ]:
# ## https://www.elportaldemusica.es/lists/top-100-albums/2020/53
# 
# def cargar():
#     respuesta = messagebox.askyesno(title="Confirmar", message="¿Está seguro que quiere recargar los datos? \nEsta operación puede ser lenta")
#     if respuesta:
#         almacenar_datos()
# 
# 
# 
# 
# 
# 
# def recibir_datos():
#     f = urllib.request.urlopen("https://www.elportaldemusica.es/lists/top-100-albums/2020/53")
#     s = BeautifulSoup(f, "lxml")
#     lista = []
#     lista_albumes = s.find("div", class_="list-view").find_all("a")
#     for link_album in lista_albumes:
#         f = urllib.request.urlopen("https://www.elportaldemusica.es"+link_album.get('href'))
#         s = BeautifulSoup(f, "lxml")
#         datos = s.find("div", class_="container-fluid text-center").div
#         ranking = datos.find("div", class_="publication_relevant").find("p", class_="single-list-entry-rank-position")
#         if(ranking == None):
#             ranking = 0
#         else:
#             ranking = ranking.string
#         print(ranking)
#         nombre = datos.find("div", class_="name").string
#         autor = datos.find("div", class_="subname").find("a", class_="external").string
#         print(autor)
#         semanas_en_lista = datos.find("div",class_="list_week").string
#         #aqui se guarda solo el numero de las semanas que lleva en la lista,
#         #Ejemplo: 4 Semanas en la lista -> guarda el 4
#         semanas = semanas_en_lista.split(sep="S")[0]
#         print(semanas)
#         print(semanas_en_lista)
#         
#         maxPosicion = datos.find("div", class_="max_pos").string
#         discografica = datos.find("div", class_="detail_one").string
#         premios = datos.find("span", class_="number").string
#         lista.append((nombre, autor))
#        #print(premios)
# 
# recibir_datos()
# 
# 
# # In[ ]:
# def almacenar_datos():
#     
#     # define el esquema de la informaciÃ³n
#     schem = Schema(nombre=TEXT(stored=True), autor=TEXT(stored=True))
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
#     lista = recibir_datos()
#     for album in lista:
#         # aÃ±ade cada pelicula de la lista al Ã­ndice
#         writer.add_document(nombre=str(album[0]), titulo_original=str(album[1]))    
#         i += 1
#     writer.commit()
#     messagebox.showinfo("Fin de indexado", "Se han indexado " + str(i) + " albumes") 
#     
# 
# def buscar_titulo_sinopsis():
# 
#     def mostrar_lista(event):
#         # abrimos el Ã­ndice
#         ix = open_dir("Index")
#         # creamos un searcher en el Ã­ndice    
#         with ix.searcher() as searcher:
#             # se crea la consulta: buscamos en los campos "titulo" o "sinopsis" alguna de las palabras que hay en el Entry "en"
#             # se usa la opciÃ³n OrGroup para que use el operador OR por defecto entre palabras, en lugar de AND
#             query = MultifieldParser(["nombre", "autor"], ix.schema, group=OrGroup).parse(str(en.get()))
#             # llamamos a la funciÃ³n search del searcher, pasÃ¡ndole como parÃ¡metro la consulta creada
#             results = searcher.search(query)  # sólo devuelve los 10 primeros
#             # recorremos los resultados obtenidos(es una lista de diccionarios) y mostramos lo solicitado
#             v = Toplevel()
#             v.title("Listado de Albumes")
#             v.geometry('800x150')
#             sc = Scrollbar(v)
#             sc.pack(side=RIGHT, fill=Y)
#             lb = Listbox(v, yscrollcommand=sc.set)
#             lb.pack(side=BOTTOM, fill=BOTH)
#             sc.config(command=lb.yview)
#             # Importante: el diccionario solo contiene los campos que han sido almacenados(stored=True) en el Schema
#             for r in results: 
#                 lb.insert(END, r['nombre'])
#                 lb.insert(END, r['autor'])
#                 lb.insert(END, '')
#     
#     v = Toplevel()
#     v.title("Busqueda por Nombre o Autor")
#     l = Label(v, text="Introduzca las palabras a buscar:")
#     l.pack(side=LEFT)
#     en = Entry(v)
#     en.bind("<Return>", mostrar_lista)
#     en.pack(side=LEFT)

