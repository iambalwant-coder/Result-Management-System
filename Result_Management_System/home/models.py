from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    math = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()
    total_marks = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=10, blank=True, null=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Updated field
