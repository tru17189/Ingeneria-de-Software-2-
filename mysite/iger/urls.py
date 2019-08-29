
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instructions', views.instructions, name='instructions'),
    path('carnet', views.carnet, name='carnet'),
    path('nombre', views.nombre, name='nombre'),
    path('students',views.students,name='students'),
	path('Cuarto1',views.Cuarto1,name='Cuarto1'),
    path('students/<str:student_carnet>/', views.detail, name='detail'),
    path('circles/create',views.create_circle,name='create_circle')
    ]
