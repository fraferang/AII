from django.urls import path
from django.contrib import admin
from main import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('carga/',views.carga),
    path('albumes/', views.lista_albumes),
    path('album-por-ranking/', views.lista_album_ranking),
    path('albumes-busqueda-por-autor/', views.buscar_albumes_autor),
    path('albumes-busqueda-por-semanas/', views.buscar_albumes_semanas),
    path('carga_whoohs/', views.mostrar_titulo_autor)
    
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
