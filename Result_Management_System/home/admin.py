from django.contrib import admin
from.models import Student

# Register your models here.

class Student_ModelAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'student_name', 'math', 'science', 'english', 'total_marks')


admin.site.register(Student, Student_ModelAdmin)
