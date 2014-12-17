from django.shortcuts import render
from address.models import Address


def address_list(request):
    print request.method
    print request.GET
    print request.POST
    addressl = Address.objects.all()
    return render(request, 'address/list.html', {'addressl': addressl})

def address_item(request, address_id):
    address = Address.objects.get(id=address_id)
    return render(request, 'address/item.html', {'address': address})
