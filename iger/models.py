from django.db import models
#Clase modelo para almacenar los datos de los estudiantes en la base de datos
#El modelo tiene los siguientes atributos del estudiante:
#carnet,nombre_completo,grado,semestre,circulo
class Student(models.Model):
    carnet = models.CharField(max_length=15, primary_key=True)
    nombre_completo = models.CharField(max_length=35)
    grado = models.IntegerField()
    semestre = models.IntegerField()
    circulo = models.ForeignKey('Circle', models.SET_NULL, blank=True, null=True)
    ingreso = models.IntegerField(default=0, editable=False)
    # def __str__(self):
    #     return self.carnet
    #Funciones Get para obtener todos los atributos del modelo de estudiante
    def get_name(self):
        return self.nombre_completo
    def get_grade(self):
        return self.grado
    def get_semester(self):
        return self.semestre
    def get_ingreso(self):
        return self.ingreso


    
#Clase modelo para almacenar los datos de los departamentos siguiendo el formato dado por IGER
#El modelo tiene los siguientes atributos del departamento:
#coordinacion(codigo),departamento(codigo)
class ListaDepartamento(models.Model):
    coordinacion = models.CharField(max_length=2, primary_key=True)
    departamento = models.CharField(max_length=30)
    ingreso = models.IntegerField(default=0, editable=False)
    #Funciones Get para obtener todos los atributos del modelo de departamento
    def get_departamento(self):
        return self.departamento
    def get_coordinacion(self):
        return self.coordinacion
    def get_ingreso(self):
        return self.ingreso
    
#Clase modelo para almacenar los datos de los circulos de estudio siguiendo el formato dado por IGER
#El modelo tiene los siguientes atributos del departamento:
#codigo_circulo,coordinacion(codigo)
class Circle(models.Model):
    codigo_circulo = models.CharField(max_length=20, primary_key=True)
    coordinacion = models.ForeignKey('ListaDepartamento', models.CASCADE)
    ingreso = models.IntegerField(default=0, editable=False)
    #Funciones Get para obtener todos los atributos del modelo de circulo
    def get_circle_code(self):
        return self.codigo_circulo
    def get_name_coor(self):
        return self.coordinacion
    def get_ingreso(self):
        return self.ingreso

class CircleSummary(Circle):
    class Meta:
        proxy = True
        verbose_name ='Ingreso circulo'
        verbose_name_plural = 'Ingresos circulos'

    #def __str__(self):
        #return self.id_coor + self.num_x + self.circle_number
