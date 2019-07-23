
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',TemplateView.as_view(template_name='home.html'), name = 'home'),
    path('<str:student_carnet>/', views.detail, name='detail'),
    ]
