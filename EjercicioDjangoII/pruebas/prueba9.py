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
    f = urllib.request.urlopen("https://entradas.correos.es/categoria/conciertos-98?page=1")
    s = BeautifulSoup(f, "lxml")
    lista_albumes = s.find("div", class_="package-list-item-wrapper on-page-result-page").find_all("div")
    for link_album in lista_albumes:
        f = urllib.request.urlopen("https://entradas.correos.es"+link_album.a['href'])  
        s = BeautifulSoup(f, "lxml")
        datos = s.find("div", class_="main-wrapper")
        concierto = datos.find("div", class_="flex-column flex-md-8 flex-sm-12").find("h1", class_="hero-title").string
        lugar = datos.find("div", class_="raty-wrapper").find("span", style="display: block;").string


# def recibir_datos():
#     f = urllib.request.urlopen("https://www.eventbrite.es/d/spain/music--events/?page=1")
#     s = BeautifulSoup(f, "lxml")
#     lista_albumes = s.find("ul", class_="search-main-content__events-list").find_all("li")
#     for link_album in lista_albumes:
#         f = urllib.request.urlopen(link_album.a['href'])
#         s = BeautifulSoup(f, "lxml")
#         datos = s.find("div", class_="g-group")
#         print(datos)
#         concierto = datos.find("div", class_="eds-text-color--primary-brand eds-l-pad-bot-1 eds-text-weight--heavy eds-text-bs")
#         print(concierto)
   
        
        


# In[3]:


recibir_datos()


# In[ ]:




