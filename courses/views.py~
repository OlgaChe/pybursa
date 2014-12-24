from django.shortcuts import render, get_object_or_404

from courses.models import Course, CourseForm


def courses_list(request):
    print request.method
    print request.GET
    print request.POST
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_add_edit(request, course_id = None):
    course = None
    if course_id is not None:
        course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save() 
            return redirect('course-edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form, 'title': title}) 

'''
def course_edit(request, course_id):
    course = Course.objects.get(id=course_id) 
    if request.method == 'post':
        form = CourseForm(request.POST, instance=course)
    if form.is_valid():
        course = form.save(instance=course) 
        print form.cleaned_data
        return redirect('course_list', course_id)
    else:
        form = CoachForm()
    return render(request, 'courses/edit.html',{'form': form}) 

def course_add(request):
    title = "Course add item"
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course-edit', course.id)
        else:
            form = CourseModelForm()
        return render(request, 'courses/edit.html', {'form': form, 'title': title}) 
'''
