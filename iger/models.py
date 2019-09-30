from django.db import models

class Student(models.Model):
    carnet = models.CharField(max_length=15, primary_key=True)
    nombre_completo = models.CharField(max_length=35)
    grado = models.IntegerField()
    semestre = models.IntegerField()
    circulo = models.ForeignKey('Circle', models.SET_NULL, blank=True, null=True)
    ingreso = models.IntegerField()
    # def __str__(self):
    #     return self.carnet
    def get_name(self):
        return self.nombre_completo
    def get_grade(self):
        return self.grado
    def get_semester(self):
        return self.semestre

class ListaDepartamento(models.Model):
    coordinacion = models.CharField(max_length=2)
    departamento = models.CharField(max_length=30, primary_key=True)
    def get_departamento(self):
        return self.departamento

    def get_coordinacion(self):
        return self.coordinacion

class Circle(models.Model):
    codigo_circulo = models.CharField(max_length=20, primary_key=True)
    coordinacion = models.ForeignKey('ListaDepartamento', models.CASCADE)

    def get_circle_code(self):
        return self.codigo_circulo

    def get_name_coor(self):
        return self.coordinacion

    #def __str__(self):
        #return self.id_coor + self.num_x + self.circle_number
