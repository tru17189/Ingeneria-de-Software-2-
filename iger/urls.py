
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
    path('students/<str:student_carnet>/', views.detail, name='detail'),
    path('circles/create',views.create_circle,name='create_circle'),
	path('students/31082019/libro_mate', views.libro_mate, name='libro_mate')
    ]
