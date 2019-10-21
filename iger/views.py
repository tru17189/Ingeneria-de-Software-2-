from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Student, Circle, ListaDepartamento
from django.http import Http404
from django.http import HttpResponse

def index(request):
    return render(request, 'iger/index.html')

def instructions(request):
    return render(request, 'iger/instructions.html')

def visitante(request):
    return render(request, 'iger/visitante.html')

def carnet(request):
    return render(request, 'iger/carnet.html')

def libro(request):
    return render_to_response('iger/Libros/English/story_html5.html')

def libro_Visita(request):
    return render(request, 'iger/Libros/visualizadores/libroVisita.html')
	
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


def error_404_view(request, exception):
    return render(request, 'iger/404.html', status=404)

def error_500_view(request):
    data ={}
    return render(request, 'iger/404.html', data)
    
def portal(request):
    carnet = ''
    nombre_completo = ''
    if request.method == 'POST':
        carnet = request.POST['numero'] 
        print(carnet)
    try:
        student = Student.objects.get(carnet=carnet)         
    except Student.DoesNotExist:
        try:
            student = Student.objects.get(nombre_completo=nombre_completo)
        except Student.DoesNotExist:
            
            return render(request, 'iger/404.html') 
            #return HttpResponse(status=500) 
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

def detail(request):
    carnet = ''
    nombre_completo = ''
    if request.method == 'POST':
        carnet = request.POST['numero'] 
        print(carnet)
    try:
        student = Student.objects.get(carnet=carnet)
        circle = Circle.objects.get(pk=student.circulo.codigo_circulo)
        coordination = ListaDepartamento.objects.get(coordinacion=circle.coordinacion.coordinacion)
        coordination.ingreso += 1
        circle.ingreso += 1
        student.ingreso += 1
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
    
    

