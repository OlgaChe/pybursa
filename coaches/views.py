from django.shortcuts import render, get_object_or_404
from coaches.models import Coach, CoachForm


def coaches_list(request):
    print request.method
    print request.GET
    print request.POST
    coaches = Coach.objects.all()
    return render(request, 'coaches/list.html', {'coaches': coaches})

def coach_info(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_detail.html', {'coach': coach})

def coach_add_edit(request, coach_id = None):
    coach = None
    if coach_id is not None:
        coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            coach = form.save() 
            return redirect('coach-edit', coach.id)
    else:
        form = CoachModelForm(instance=coach)
    return render(request, 'coaches/edit.html', {'form': form, 'title': title}) 


'''
def coach_edit(request, coach_id):
    coach = Coach.objects.get(id=coach_id) 
    if request.method == 'post':
        form = CoachForm(request.POST, instance=coach)
    if form.is_valid():
        coach = form.save() 
        print form.cleaned_data
        return redirect('coach_list', coach_id)
    else:
        form = CoachForm(instance=coach)
    return render(request, 'coaches/edit.html',{'form': form}) 

def coach_add(request):
    title = "Coach add item"
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            coach = form.save()
            return redirect('coach-edit', coach.id)
        else:
            form = CoachModelForm()
        return render(request, 'coaches/edit.html', {'form': form, 'title': title}) 
'''
