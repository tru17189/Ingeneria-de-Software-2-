
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views
#Diferentes direcciones URL que utiliza el proyecto y los views que utiliza
#Los url que se encuentran son aquellos que cargan la vista de lo siguiente:
#Ingreso de Carnet, Instrucciones para descarga de libros, Vista de libros disponibles
#Visualizador de libro de matematica, ingles y fisica
urlpatterns = [
    path('', views.carnet, name='carnet'),
    path('visitante', views.visitante, name='visitante'),
    path('instructions', views.instructions, name='instructions'),
    path('instructions2', views.instructions2, name='instructions2'),
    path('nombre', views.nombre, name='nombre'),
    path('student', views.detail, name='detail'),
    path('students', views.portal, name='portal'),
    path('', include('pwa.urls')),
    path('pdf_view', views.pdf_view, name='pdf_view'),
    path(r'adminactions/', include('adminactions.urls')),
    ]
