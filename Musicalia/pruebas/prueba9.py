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


# def recibir_datos():
#     f = urllib.request.urlopen("https://www.eventbrite.es/d/spain/music--events/?page=1")
#     s = BeautifulSoup(f, "lxml")
#     lista_albumes = s.find("ul", class_="search-main-content__events-list").find_all("div", class_="eds-event-card-content__primary-content")
#     print(lista_albumes)
#     for link_album in lista_albumes:
#         f = urllib.request.urlopen("https://www.eventbrite.es"+link_album.a['href'])
#         s = BeautifulSoup(f, "lxml")

   
        
        


# In[3]:


#recibir_datos()


# In[ ]:




