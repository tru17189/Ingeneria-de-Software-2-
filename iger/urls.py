
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.carnet, name='carnet'),
    path('instructions', views.instructions, name='instructions'),
    path('nombre', views.nombre, name='nombre'),
    path('students',views.students,name='students'),
    path('students/31082019/Libro', views.libro, name="Libro"),
    path('students/<str:carnet>/', views.detail, name='detail'),
	path('students/31082019/libro_mate', views.libro_mate, name='libro_mate'),
	path('students/31082019/libro_mate1', views.libro_mate1, name='libro_mate1'),
	path('students/31082019/libro_Ingles1', views.libro_Ingles1, name='libro_Ingles1'),
	path('students/31082019/libro_Fisica1', views.libro_Fisica1, name='libro_Fisica1')
    ]
