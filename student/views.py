from django.shortcuts import render
from student.models import Student, StudentForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import FormView


class StudentView(ListView):
    template_name = "student/list.html"
    model= Student
    queryset = Student.objects.filter(package='standart')
    def get_queryset(self):
        filter_package = self.request.GET.get('package', 'standart')
        return Student.objects.filter(package= filter_package)

class StudentView(DetailView):
    template_name = 'student/item.html'
    model = Student 

class StudentEditForm(FormView):
    template_name = 'student/edit.html'
    form_class = StudentForm
    success_url = '/student/list/'
    def form_valid(self, form):
        return super(StudentEditForm, self).form_valid(form)

def students_list(request):
    print request.method
    print request.GET
    print request.POST
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})

def students_item(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student/item.html', {'student': student})

def student_edit(request, student_id):
    student = Student.objects.get(id=student_id) 
    if request.method == 'post':
        form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        student = form.save() 
        print form.cleaned_data
        return redirect('student_list', student_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/edit.html',{'form': form}) 

def student_add(request):
    title = "Student add item"
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student-edit', student.id)
        else:
            form = StudentModelForm()
        return render(request, 'student/edit.html', {'form': form, 'title': title}) 
