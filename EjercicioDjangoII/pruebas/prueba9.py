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
    f = urllib.request.urlopen("https://www.eventbrite.es/d/spain/music--events/?page=1")
    s = BeautifulSoup(f, "lxml")
    lista_albumes = s.find("ul", class_="search-main-content__events-list").find_all("li")
    print(lista_albumes)
    for link_album in lista_albumes:
        print(link_album.get('href'))
        f = urllib.request.urlopen("https://www.eventbrite.es/"+link_album.get('href'))
        s = BeautifulSoup(f, "lxml")
        datos = s.find("ul", class_="search-main-content__events-list")
        print(datos)
    
        
        
        


# In[3]:


recibir_datos()


# In[ ]:




