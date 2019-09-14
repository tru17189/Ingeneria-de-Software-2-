from django.contrib import admin
from .models import Student
from .models import ListaDepartamento
from .models import Circle
from .forms import ListaDepartamentoForm


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('student_carnet', 'student_name', 'student_grade', 'student_semester')
    list_filter = ('student_grade', 'student_semester')


class CyD(admin.ModelAdmin):
    form = ListaDepartamentoForm

admin.site.register(Student, AuthorAdmin) 
admin.site.register(ListaDepartamento, CyD)
admin.site.register(Circle)