from django.test import TestCase
from .models import Student
from .models import ListaDepartamento
from .models import Circle

from .views import libro_mate


# Create your tests here.

class StudentTestCase(TestCase):
    def test_get_student(self):
        ListaDepartamento.objects.create(coordinacion = "02", departamento="Guatemala 2")
        depa = ListaDepartamento.objects.get(pk="Guatemala 2")
        Circle.objects.create(codigo_circulo="010203", coordinacion=depa)
        circulo = Circle.objects.get(pk="010203")
        Student.objects.create(carnet="101", nombre_completo="John Doe",grado=1,semestre=2, circulo=circulo)
        estudiante = Student.objects.get(pk="101")
        self.assertEqual(estudiante.carnet, '101')
        self.assertEqual(estudiante.nombre_completo, 'John Doe')
        self.assertEqual(estudiante.grado, 1)
        self.assertEqual(estudiante.semestre, 2)
        self.assertEqual(estudiante.circulo, circulo)

class ListaDepartamentoTestCase(TestCase):
    def test_get_ListaDepartamento(self):
        ListaDepartamento.objects.create(coordinacion = "02", departamento="Guatemala 2")
        pruebaDepartamento = ListaDepartamento.objects.get(pk="Guatemala 2")
        self.assertEqual(pruebaDepartamento.coordinacion, '02')
        self.assertEqual(pruebaDepartamento.departamento, 'Guatemala 2')


class createCircleTestCase(TestCase):
   def test_get_createCircle(self):
       ListaDepartamento.objects.create(coordinacion = "02", departamento="Guatemala 2")
       depa = ListaDepartamento.objects.get(pk="Guatemala 2")
       Circle.objects.create(codigo_circulo="010203", coordinacion=depa)
       pruebaCirculo = Circle.objects.get(pk="010203")
       self.assertEqual(pruebaCirculo.codigo_circulo, '010203')
       self.assertEqual(pruebaCirculo.coordinacion, depa)

