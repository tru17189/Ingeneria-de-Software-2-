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
    return render(request, 'iger/Libros/4to(primer_semestre)/Matematica_Financiera/story_html5.html')

def nombre(request):
    return render(request, 'iger/nombre.html')
	
def pantallaTemporal(request):
    return render(request, 'iger/pantallaTemporal.html')

def students(request):
    carnet_list = Student.objects.all()
    context = {'carnet_list': carnet_list}
    return render(request, 'iger/students.html', context)


def detail(request, student_carnet):
    try:
        student = Student.objects.get(student_carnet=student_carnet)         
    except Student.DoesNotExist:
        try:
            student = Student.objects.get(student_name=student_carnet)
        except Student.DoesNotExist:
            raise Http500("El alumno no existe, ingrese nuevamente sus credenciales")
    
    if (student.student_grade == 4):
        if(student.student_semester == 1):
            return render(request, 'iger/semester.html', {'student': student})
        else:
            return render(request, 'iger/Semester2.html', {'student': student})
    else:
        if(student.student_semester == 1):
            return render(request, 'iger/QuintoSemester.html', {'student': student})
        else:
            return render(request, 'iger/QuintoSemester2.html', {'student': student})
    
    

