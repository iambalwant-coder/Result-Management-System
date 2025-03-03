from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student

# Create your views here.

def home_views(request):
    students = Student.objects.all()

    # Filtering by student name
    name_query = request.GET.get('name', '')
    if name_query:
        students = students.filter(student_name__icontains=name_query)

    # Filtering by result status
    result_query = request.GET.get('result', '')
    if result_query in ['PASS', 'FAIL']:
        students = students.filter(result=result_query)

    return render(request, 'home.html', {'students': students, 'name_query': name_query, 'result_query': result_query})


# def home_views(request):
#     students = Student.objects.all()
#     return render(request, 'home.html', {'students': students})

def add_views(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name =request.POST.get('student_name')
        math =request.POST.get('math')
        science =request.POST.get('science')
        english =request.POST.get('english')
        
        t = int(math) + int(english) + int(science)
        total_marks = t
        if int(math) >= 35 and int(english) >= 35 and int(science) >= 35 and total_marks >= (35*3):
            f ='PASS'
        else:
            f ='FAIL'
        
        # Calculate percentage
        percentage = (total_marks/300) * 100

        s=Student()

        s.student_id = student_id
        s.student_name = student_name
        s.math = math
        s.english = english
        s.science = science
        s.total_marks = total_marks
        s.result = f
        s.percentage = percentage

        s.save()
        return redirect('/')
    else:
        return render(request,'add.html')

def delete_views(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/')

def edit_views(request, id):
    student = Student.objects.get(pk=id)
    
    if request.method == 'POST':
        # Update student data based on form input
        student.student_id = request.POST.get('student_id')
        student.student_name = request.POST.get('student_name')
        student.math = request.POST.get('math')
        student.science = request.POST.get('science')
        student.english = request.POST.get('english')

        # Calculate total marks and determine result
        total_marks = int(student.math) + int(student.english) + int(student.science)
        student.total_marks = total_marks

        if int(student.math) >= 35 and int(student.english) >= 35 and int(student.science) >= 35 and total_marks >= (35 * 3):
            student.result = 'PASS'
        else:
            student.result = 'FAIL'
        
        # Calculate percentage
        student.percentage = (total_marks / 300) * 100

        # Update student record with new data
        student.save()
        
        return redirect('/')

        # Save updated student record
        student.save()
        
        return redirect('/')
    
    return render(request, 'edit.html', {'student': student})

def view(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'view.html', {'student': student})

def about(request):
    return render(request, 'about.html')
