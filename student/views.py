from django.shortcuts import render
from student.models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})

def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student/item.html', {'student': student})
