from django.urls import path
from django.contrib import admin
from main import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('carga/',views.carga),
    path('albumes/', views.lista_albumes),
    path('album-por-ranking/', views.lista_album_ranking),
    path('albumes-busqueda-por-autor/', views.buscar_albumes_autor),
    path('albumes-busqueda-por-semanas/', views.buscar_albumes_semanas)

    ]
