from django.db import models

class Student(models.Model):
    student_carnet = models.CharField(max_length=15, primary_key=True)
    student_name = models.CharField(max_length=50)
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

