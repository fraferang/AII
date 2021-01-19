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
    lista_albumes = s.find("div", class_="package-list-item-wrapper").find_all("div")
    for link_album in lista_albumes:
        f = urllib.request.urlopen(link_album.a['href'])    
        s = BeautifulSoup(f, "lxml")
        datos = s.find("div", class_="package-list-item")
        concierto =datos.find("div", class_="content").find("h4", class_="mb-0").find("a").string
        Lugar = datos.find("ul", class_="list-info").find("span" , class_="font600").string
#         concierto = datos.find("div", class_="eds-text-color--primary-brand eds-l-pad-bot-1 eds-text-weight--heavy eds-text-bs")
#         print(concierto)

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




