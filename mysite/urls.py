"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler404
#Se definen las diferentes bases de url para posibles aplicaciones que contiene el proyecto,
#en nuestro caso se define que la url base es para los url de la aplicacion principal de iger
#y. en admin se coloca todo lo del modulo del administrador
urlpatterns = [
    path('', include('iger.urls')),
    path('home/',TemplateView.as_view(template_name='home.html'), name = 'home'),
    path('admin/', admin.site.urls),
]
#Se definen las vistas para el manejador de errores para errores 404 y 500 que se muestran
#para toda la aplicacion

handler404 = 'iger.views.error_404_view'
handler500 = 'iger.views.error_500_view'
urlpatterns += staticfiles_urlpatterns()
