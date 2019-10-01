from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Student, Circle
from django.http import Http404

def index(request):
    return render(request, 'iger/index.html')

def instructions(request):
    return render(request, 'iger/instructions.html')

def carnet(request):
    return render(request, 'iger/carnet.html')

def libro(request):
    return render_to_response('iger/Libros/English/story_html5.html')
	
def libro_mate(request):
    return render(request, 'booksIger/Matematica_Financiera/story_html5.html')
	
def libro_mate1(request):
    return render(request, 'iger/Libros/visualizadores/libroMate.html')
	
def libro_Ingles1(request):
    return render(request, 'iger/Libros/visualizadores/libroIngles.html')
	
def libro_Fisica1(request):
    return render(request, 'iger/Libros/visualizadores/libroFisica.html')
	
def libro_FisicaHTML(request):
    return render(request, '../../booksIger/Fisica4to/story.html')

def nombre(request):
    return render(request, 'iger/nombre.html')
	
def pantallaTemporal(request):
    return render(request, 'iger/pantallaTemporal.html')

def students(request):
    carnet_list = Student.objects.all()
    context = {'carnet_list': carnet_list}
    return render(request, 'iger/students.html', context)

def error_404_view(request, exception):
    return render(request, 'iger/404.html', status=404)

def error_500_view(request):
    data ={}
    return render(request, 'iger/404.html', data)
    
def detail(request, carnet):
    try:
        student = Student.objects.get(carnet=carnet)         
    except Student.DoesNotExist:
        try:
            student = Student.objects.get(nombre_completo=nombre_completo)
        except Student.DoesNotExist:
            raise Http500("El alumno no existe, ingrese nuevamente sus credenciales")
    
    if (student.grado == 4):
        if(student.semestre == 1):
            return render(request, 'iger/semester.html', {'student': student})
        else:
            return render(request, 'iger/Semester2.html', {'student': student})
    else:
        if(student.semestre == 1):
            return render(request, 'iger/QuintoSemester.html', {'student': student})
        else:
            return render(request, 'iger/QuintoSemester2.html', {'student': student})
    
    

