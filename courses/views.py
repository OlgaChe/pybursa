from django.shortcuts import render, get_object_or_404

from courses.models import Course


def courses_list(request):
    print request.method
    print request.GET
    print request.POST
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_edit(request):
    if request.method == 'post':
    form = CourseForm(request.POST)
    if form.is_valid():
        print form.cleaned_data
        return redirect('course_list')
    else:
        form = CoachForm()
    return render(request, 'courses/edit.html',{'form': form}) 
