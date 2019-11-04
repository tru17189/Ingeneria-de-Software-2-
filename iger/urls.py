
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
    path('nombre', views.nombre, name='nombre'),
    path('student', views.detail, name='detail'),
    path('students', views.portal, name='portal'),
	path('libro_LenguaLiteratura1', views.libro_LenguaLiteratura1, name='libro_LenguaLiteratura1'),
	path('libro_mate1', views.libro_mate1, name='libro_mate1'),
	path('libro_Ingles1', views.libro_Ingles1, name='libro_Ingles1'),
	path('libro_Fisica1', views.libro_Fisica1, name='libro_Fisica1'),
    path('', include('pwa.urls'))
    ]
