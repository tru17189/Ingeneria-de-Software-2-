from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Circle
from django.http import Http404

def index(request):
    return render(request, 'iger/index.html')

def instructions(request):
    return render(request, 'iger/instructions.html')

def carnet(request):
    return render(request, 'iger/carnet.html')

def nombre(request):
    return render(request, 'iger/nombre.html')
	
def Cuarto1(request):
    return render(request, 'iger/Grades_Views/4to1Semester.html')

def students(request):
    carnet_list = Student.objects.all()
    print(carnet_list)
    context = {'carnet_list': carnet_list}
    return render(request, 'iger/students.html', context)

def create_circle(request):
    coor_list = [
        {'id': '01','name': 'COBÁN'},
        {'id': '07','name': 'CENTROS ESPECIALES'},
        {'id': '03','name': 'CHIMALTENANGO'},
        {'id': '09','name': 'EL ESTOR'},
        {'id': '02','name': 'SALAMA'},
        {'id': '04','name': 'CHIQUIMULA'},
        {'id': '12','name': 'POPTÚN'},
        {'id': '06','name': 'ESCUINTLA'},
        {'id': '07','name': 'GUATEMALA'},
        {'id': '08','name': 'HUEHUETENANGO'},
        {'id': '09','name': 'IZABAL'},
        {'id': '10','name': 'JALAPA'},
        {'id': '11','name': 'JUTIAPA'},
        {'id': '13','name': 'QUETZALTENANGO'},
        {'id': '14','name': 'EL QUICHÉ'},
        {'id': '04','name': 'ZACAPA'},
        {'id': '17','name': 'SAN MARCOS'},
        {'id': '18','name': 'SANTA ROSA'},
        {'id': '19','name': 'SOLOLÁ'},
        {'id': '13','name': 'RETALHULEU'},
        {'id': '12','name': 'SAYAXCHÉ'}
    ]
    coor, num_circle, num_x = request.GET.get('coor'), request.GET.get('num_circle'), request.GET.get('num_x')
    if coor and num_circle and num_x:
        circle_code = coor + num_x + num_circle
        for i in coor_list:
            if coor == i['id']:
                name_coor = i['name']
        Circle(circle_code=circle_code, name_coor=name_coor, id_coor=coor, num_x=num_x, circle_number=num_circle).save()
        context = {'coor_list': coor_list, 'saved':True}
    else:
        context = {'coor_list': coor_list, 'saved':False}
    return render(request,'circles/create.html', context)

def detail(request, student_carnet):
    try:
        student = Student.objects.get(student_carnet=student_carnet)         
    except Student.DoesNotExist:
        try:
            student = Student.objects.get(student_name=student_carnet)
        except Student.DoesNotExist:
            raise Http500("El alumno no existe, ingrese nuevamente sus credenciales")
    return render(request, 'iger/detail.html', {'student': student})

