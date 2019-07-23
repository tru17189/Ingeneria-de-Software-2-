from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.http import Http404
def index(request):
    carnet_list = Student.objects.all()
    print(carnet_list)
    context = {'carnet_list': carnet_list}
    return render(request, 'iger/index.html', context)

def detail(request, student_carnet):
    try:
        student = Student.objects.get(pk=student_carnet)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'iger/detail.html', {'student': student})
# Create your views here.
