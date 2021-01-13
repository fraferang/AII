from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('carga/',views.carga),
    path('albumes/', views.lista_albumes),
    path('albumesporranking/', views.lista_albumesporranking),
    ]
