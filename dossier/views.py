from django.shortcuts import render
from dossier.models import Dossier


def dossier_list(request):
    dossierl = Dossier.objects.all()
    return render(request, 'dossier/list.html', {'dossierl': dossierl})

def dossier_item(request, dossier_id):
    dossier = Dossier.objects.get(id=dossier_id)
    return render(request, 'dossier/item.html', {'dossier': dossier})


