from django.shortcuts import render, get_object_or_404
from coaches.models import Coach


def coaches_list(request):
    print request.method
    print request.GET
    print request.POST
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})

def coach_info(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_detail.html', {'coach': coach})

def coach_edit(request):
    if request.method == 'post':
    form = CoachForm(request.POST)
    if form.is_valid():
        print form.cleaned_data
        return redirect('coach_list')
    else:
        form = CoachForm()
    return render(request, 'coaches/edit.html',{'form': form}) 