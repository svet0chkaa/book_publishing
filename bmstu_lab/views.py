from django.shortcuts import redirect, render
from bmstu_lab.models import Requests
from bmstu_lab.models import Users
from bmstu_lab.models import Moderators
from bmstu_lab.models import Orders
from django.db.models import Q

def GetOrders(request):
    input_text = request.GET.get("find")
    input_filter = request.GET.getlist("manufacturer")

    orders = Orders.objects.order_by('id')
    orders = orders.filter(status="valid")

    if input_text:
        orders = orders.filter(title__icontains = input_text)
    else:
        input_text = ''

    if input_filter:
        filter_list = [Q(processor__icontains=filter_item) for filter_item in input_filter]
        orders = orders.filter(*filter_list)
    return render(request, 'orders.html', {'data': {
        'orders': orders,
        'query': input_text,
        'filter_list': input_filter}})

def GetOrder(request, id):
    order = Orders.objects.filter(id=id).first()
    return render(request, 'order.html', {'data': {
        'orders': order,
        }})

def delObject(request, id):
    Orders.objects.filter(id=id).update(status="deleted")
    return redirect('/')