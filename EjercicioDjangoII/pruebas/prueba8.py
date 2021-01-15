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








def recibir_datos():
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
        print(ranking)
        nombre = datos.find("div", class_="name").string
        autor = datos.find("div", class_="subname").find("a", class_="external").string
        print(autor)
        semanas_en_lista = datos.find("div",class_="list_week").string
        #aqui se guarda solo el numero de las semanas que lleva en la lista,
        #Ejemplo: 4 Semanas en la lista -> guarda el 4
        semanas = semanas_en_lista.split(sep="S")[0]
        print(semanas)
        print(semanas_en_lista)
        
        maxPosicion = datos.find("div", class_="max_pos").string
        discografica = datos.find("div", class_="detail_one").string
        premios = datos.find("span", class_="number").string
       #print(premios)
        
        


# In[3]:


recibir_datos()


# In[ ]:




