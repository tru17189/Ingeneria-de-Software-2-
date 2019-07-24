
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instructions', views.instructions, name='instructions'),
    path('students',views.students,name='students'),
    path('students/<str:student_carnet>/', views.detail, name='detail'),
    ]
