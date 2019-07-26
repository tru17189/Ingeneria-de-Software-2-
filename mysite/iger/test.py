from django.test import TestCase
from .models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def test_get_student(self):
        Student.objects.create(student_carnet="101", student_name="John Doe",student_grade=1,student_semester=2)
        estudiante = Student.objects.get(pk="101")
        self.assertEqual(estudiante.student_carnet, '101')
        self.assertEqual(estudiante.student_name, 'John Doe')
        self.assertEqual(estudiante.student_grade, 1)
        self.assertEqual(estudiante.student_semester, 2)

        
   
        
        
        
