from django.db import models

class Student(models.Model):
    student_carnet = models.CharField(max_length=15, primary_key=True)
    student_name = models.CharField(max_length=15)
    student_grade = models.IntegerField()
    student_semester = models.IntegerField()
    def __str__(self):
        return self.student_carnet
    def get_name(self):
        return self.student_name
    def get_grade(self):
        return self.student_grade
    def get_semester(self):
        return self.student_semester

class Departamento(models.Model):
    coordinacion = models.IntegerField()
    departamento = models.CharField(max_length=30, primary_key=True)
    def get_departamento(self):
        return self.departamento

class Circle(models.Model):
    circle_code = models.CharField(max_length=20, primary_key=True)
    name_coor = models.CharField(max_length=20)
    id_coor = models.IntegerField()
    num_x = models.IntegerField()
    circle_number = models.IntegerField()

    def __str__(self):
        return self.id_coor + self.num_x + self.circle_number
