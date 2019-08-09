from django.contrib import admin

from .models import Student

#admin.site.register(Student)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('student_carnet', 'student_name', 'student_grade', 'student_semester')
    list_filter = ('student_grade', 'student_semester')

admin.site.register(Student, AuthorAdmin)