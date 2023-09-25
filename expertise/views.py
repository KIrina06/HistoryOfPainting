from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Проверка подлинности', 'id': 1},
            {'title': 'Заказ копии', 'id': 2},
            {'title': 'Определение художника', 'id': 3},
            {'title': 'Определение эпохи', 'id': 4},
            {'title': 'Реставрация', 'id': 5},
            {'title': 'Заказ на разбор картины', 'id': 6},
        ]
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})