# ABCdigital [![Build Status](https://travis-ci.org/tru17189/Ingeneria-de-Software-2-.svg?branch=master)](https://travis-ci.org/tru17189/Ingeneria-de-Software-2-)

Plataforma para descargar y visualizar los libros para los diferentes grados y semestres del bachillerato digital de Iger. También cuenta con un módulo administrador en el cual se pueden agregar alumnos, circulos, coordinaciones y ver estadisticas de la cantidad de alumnos que han ingresado al portal.


### Prerequisitos

Antes de clonar el repositorio se debera de descargar lo siguiente: 
 - Python 3.x
Instalar pip y configurar python como una variable de entorno, por último correr el comando:

```
pip install django
```

### Instalación

Después de clonar el repositorio, dirigirse a la carpeta en donde se clono y correr los siguientes comandos:


```
pip install -r requirements.txt
```
Lo que este comando instala son las dependencias que utiliza el proyecto tales como sql, rest-framework, y behave-django.

Después correr los siguientes comandos para inicializar la base de datos: 

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Una vez realizado esto correr el último comando:
```
python manage.py runserver
```
Esto inicializara la aplicación en el localhost de la computadora, se puede abrir en cualquier webbrowser.


## Tests

Para verificar las pruebas unitarias se puede correr el siguiente comando: 
```
python manage.py test
```

En cuanto a pruebas BDD se necesita de un chromedriver, al tener eso correr el siguiente comando
```
python manage.py feature
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
 

## Authors

* **María Fernanda López** - [Mafer](https://github.com/diazMafer)
* **Miguel Valle** - [Mikki](https://github.com/PurpleBooth)
* **Antonio Reyes** - [Tony](https://github.com/PurpleBooth)
* **Raúl Mónzon** - [Raul](https://github.com/PurpleBooth)
* **Alexander Trujillo** - [Alex](https://github.com/PurpleBooth)


