from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from expertise.models import Expertise, Status
from django.db import connection

def GetOrders(request):
    data = {
        'title': 'Услуги',
        'orders': Expertise.objects.all()}
    
    return render(request, 'orders.html', data)

def GetOrder(request, id):
    data = {
        'title': 'Услуги',
        'orders': Expertise.objects.all()}
    order = {
        'id': id,
        'name': 'name',
        'image': 'image',
        'price': 0,
        'description': 'description',
        'status': 'null'
    }
    for i in data['orders']:
        if id == i.id:
            order['id'] = i.id
            order['name'] = i.name
            order['price'] = i.price
            order['image'] = i.image
            order['description'] = i.description
            order['status'] = i.status
    
    return render(request, 'order.html', order)

def sendText(request):
    input_text = request.POST.get('name', 'Проверка подлинности')
    data = {
        'title': 'Услуги',
        'orders': Expertise.objects.all()}
    order = {
        'id': 0,
        'name': 'name',
        'image': 'image',
        'price': 0,
        'description': 'description',
        'status': 'null',
    }
    for i in data['orders']:
        if input_text == i.name:
            order['id'] = i.id
            order['name'] = i.name
            order['price'] = i.price
            order['image'] = i.image
            order['description'] = i.description
            order['status'] = i.status
    return render(request, 'order.html', order)

def delExp(request):
    input_text = request.POST.get('name', 'Проверка подлинности')
    order = {
        'id': 0,
        'name': 'name',
        'image': 'image',
        'price': 0,
        'description': 'description',
        'status': 'null'
    }
    with connection.cursor() as cursor:
        cursor.execute('UPDATE Expertise SET status="удалён" WHERE name = %s', [input_text])
    data = {
        'title': 'Услуги',
        'orders': Expertise.objects.all()}
    for i in data['orders']:
        if input_text == i.name:
            order['id'] = i.id
            order['name'] = i.name
            order['price'] = i.price
            order['image'] = i.image
            order['description'] = i.description
            order['status'] = i.status
    return render(request, 'order.html', order)