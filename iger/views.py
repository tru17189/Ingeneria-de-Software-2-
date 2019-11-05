from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Student, Circle, ListaDepartamento
from django.http import FileResponse, Http404
from django.http import HttpResponse
#Lista de diferentes vistas de  la aplicacion y los procesos que
#se realizan antes de cargar la pagina solicitada

def pdf_view(request):
    try:
        return FileResponse(open('iger/Contabilidad_tacana_5_8.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
def index(request):
    return render(request, 'iger/index.html')
#Vista de instrucciones para los estudiantes para la descarga y lectura
#de los libros electroncos
def instructions(request):
    return render(request, 'iger/instructions.html')

def instructions2(request):
    return render(request, 'iger/instructionsI.html')
#Vista de visitante que no es estudiante
def visitante(request):
    return render(request, 'iger/visitante.html')
#Vista de ingreso de carnet del estudiante
def carnet(request):
    return render(request, 'iger/carnet.html')
 
#conozca su carnet
def nombre(request):
    return render(request, 'iger/nombre.html')
	
def pantallaTemporal(request):
    return render(request, 'iger/pantallaTemporal.html')

#Vista de error en caso de que surja un error tipo 404, y que 
#pueda regresar a la pagina de inicio
def error_404_view(request, exception):
    return render(request, 'iger/404.html', status=404)
#Vista de error en caso de que surja un error tipo 500, y que 
#pueda regresar a la pagina de inicio
def error_500_view(request):
    data ={}
    return render(request, 'iger/404.html', data)
#Vista de libros disponibles que previamente a cargar, verifica que el carnet 
#ingresado si sea uno existente, o que el nombre ingresado si pertenezca a 
#uno de los estudiantes en la base de datos.
#Luego dependiendo del grado y semestre del estudiante, carga la lista de libros 
#necesaria
def portal(request):
    #Se definen las variables para asignar valores del carnet y nombre de usuario
    carnet = ''
    nombre_completo = ''
    #Se verifica que se ha llegado a este view por medio de un metodo de post por un submit 
    if request.method == 'POST':
	#Se obtiene el valor pasado por el submit donde se obtiene el carnet del estudiante
        carnet = request.POST['numero'] 
        print(carnet)
    #Se intenta obtener el modelo del estudiante buscandolo por su carnet
    try:
        student = Student.objects.get(carnet=carnet)         
    except Student.DoesNotExist:
	#Si no se logra encontrar el estudiante por carnet se busca por nombre
        try:
            student = Student.objects.get(nombre_completo=nombre_completo)
        except Student.DoesNotExist:
            #Si no se enceuntra se carga el view de error de 404
            return render(request, 'iger/404.html') 
            #return HttpResponse(status=500) 
    #Dependiendo del grado del estudiante se carga la vista correspondiente
    if (student.grado == 4):
        if(student.semestre == 1):
            return render(request, 'semester.html', {'student': student})
        else:
            return render(request, 'iger/Semester2.html', {'student': student})
    else:
        if(student.semestre == 1):
            return render(request, 'iger/QuintoSemester.html', {'student': student})
        else:
            return render(request, 'iger/QuintoSemester2.html', {'student': student})
#Proceso por el cual obtenemos la informacion para generar las estadisticas de 
#la cantidad de veces que un estudiante ha ingresado a una de las paginas de 
#la aplicacion
def detail(request):
    #Se definen las variables para asignar valores del carnet y nombre de usuario
    carnet = ''
    nombre_completo = ''
    #Se verifica que se ha llegado a este view por medio de un metodo de post por un submit 
    if request.method == 'POST':
	#Se obtiene el valor pasado por el submit donde se obtiene el carnet del estudiante
        carnet = request.POST['numero'] 
        print(carnet)
    try:
	#Se busca modelo del estudiante buscandolo por su carnet
        student = Student.objects.get(carnet=carnet)
	#Se busca el circulo al que pertenece el estudiante
        circle = Circle.objects.get(pk=student.circulo.codigo_circulo)
	#Se busca la coordinacion al que pertenece el circulo del estudiante
        coordination = ListaDepartamento.objects.get(coordinacion=circle.coordinacion.coordinacion)
	#Se guarda que un estudiante de dicha coordinacion ha ingresado a la pagina
        coordination.ingreso += 1
	#Se guarda que un estudiante de el circulo ha ingresado a la pagina
        circle.ingreso += 1
	#Se guarda que un estudiante ha ingresado a la pagina
        student.ingreso += 1
	#Se guardan los valores cambiados en la base de datos
        coordination.save()
        circle.save()
        student.save()                
    except Student.DoesNotExist:
        try:
            student = Student.objects.get(nombre_completo=nombre_completo)
            circle = Circle.objects.get(pk=student.circulo.codigo_circulo)
            coordination = ListaDepartamento.objects.get(coordinacion=circle.coordinacion.coordinacion)
            coordination.ingreso += 1
            circle.ingreso += 1
            student.ingreso += 1
            coordination.save()
            circle.save()
            student.save()       
        except Student.DoesNotExist:
            return render(request, 'iger/404.html') 
            #return HttpResponse(status=500)
    
    if (student.grado == 4):
        if(student.semestre == 1):
            if(student.ingreso == 1):
                return render(request, 'iger/instructions.html')
            else:
                return render(request, 'semester.html', {'student': student})
        else:
            if(student.ingreso == 1):
                return render(request, 'iger/instructions.html')
            else:
                return render(request, 'semester.html', {'student': student})
    else:
        if(student.semestre == 1):
            if(student.ingreso == 1):
                return render(request, 'iger/instructions.html')
            else:
                return render(request, 'semester.html', {'student': student})
        else:
            if(student.ingreso == 1):
                return render(request, 'iger/instructions.html')
            else:
                return render(request, 'semester.html', {'student': student})
    
    

