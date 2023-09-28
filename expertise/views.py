from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def GetOrders(request):
    data = {
        'title': 'Услуги',
        'orders': [
            {'id': 1, 
             'name': 'Проверка подлинности',
             'price': 10000,
             'image': "https://mostmag.ru/wp-content/uploads/2020/11/a3028ac6-a555-4a08-9eda-2052f18af329.jpg",
             'description': 'Проверка картины на подлинность. Срок проверки - 3 дня. В срочном порядке - 1 день.'},
            {'id': 2, 
             'name': 'Заказ копии',
             'price': 21000,
             'image': "https://mportret.ru/upload/medialibrary/33a/33af12aefdaa37207355dab3fc2c8afe.png",
             'description': 'Срок создания копии от 7 дней до 3 месяцев в зависимости от размера и техники, в которой выполнена картина.'},
            {'id': 3, 
             'name': 'Определение художника',
             'price': 4200,
             'image': "https://dic.academic.ru/pictures/wiki/files/65/Adriaen_van_Ostade_006.jpg",
             'description': 'Не можете определить чья работа попала к Вам в руки? Мы поможем!'},
            {'id': 4, 
             'name': 'Определение эпохи',
             'price': 3700,
             'image': 'https://yantar.ua/upload/custom/images/0_ac631_dc44a423_orig.jpg',
             'description': 'Определение направления и жанра в котором писал художник. Сроки выполнения 3 - 5 дней.'},
            {'id': 5, 
             'name': 'Реставрация',
             'price': 25000,
             'image': 'https://antiquarika.ru/wp-content/uploads/2021/10/Restavratsiya-kartin.jpg',
             'description': 'Реставрация картин, выполненных маслом.'},
            {'id': 6, 
             'name': 'Заказ на разбор картины',
             'price': 5000,
             'image': "https://s5.afisha.ru/mediastorage/e4/e1/8b1fb0681b304743b342ae72e1e4.jpg",
             'description': 'Не знаете что за картина? Не проблема! Мы поможем узнать все о картине и ее создателе.'},
        ]}
    
    return render(request, 'orders.html', data)

def GetOrder(request, id):
    data = {
        'title': 'Услуги',
        'orders': [
            {'id': 1, 
             'name': 'Проверка подлинности',
             'price': 10000,
             'image': "https://mostmag.ru/wp-content/uploads/2020/11/a3028ac6-a555-4a08-9eda-2052f18af329.jpg",
             'description': 'Проверка картины на подлинность. Срок проверки - 3 дня. В срочном порядке - 1 день.'},
            {'id': 2, 
             'name': 'Заказ копии',
             'price': 21000,
             'image': "https://mportret.ru/upload/medialibrary/33a/33af12aefdaa37207355dab3fc2c8afe.png",
             'description': 'Срок создания копии от 7 дней до 3 месяцев в зависимости от размера и техники, в которой выполнена картина.'},
            {'id': 3, 
             'name': 'Определение художника',
             'price': 4200,
             'image': "https://dic.academic.ru/pictures/wiki/files/65/Adriaen_van_Ostade_006.jpg",
             'description': 'Не можете определить чья работа попала к Вам в руки? Мы поможем!'},
            {'id': 4, 
             'name': 'Определение эпохи',
             'price': 3700,
             'image': 'https://yantar.ua/upload/custom/images/0_ac631_dc44a423_orig.jpg',
             'description': 'Определение направления и жанра в котором писал художник. Сроки выполнения 3 - 5 дней.'},
            {'id': 5, 
             'name': 'Реставрация',
             'price': 25000,
             'image': 'https://antiquarika.ru/wp-content/uploads/2021/10/Restavratsiya-kartin.jpg',
             'description': 'Реставрация картин, выполненных маслом.'},
            {'id': 6, 
             'name': 'Заказ на разбор картины',
             'price': 5000,
             'image': "https://s5.afisha.ru/mediastorage/e4/e1/8b1fb0681b304743b342ae72e1e4.jpg",
             'description': 'Не знаете что за картина? Не проблема! Мы поможем узнать все о картине и ее создателе.'},
        ]}
    order = {
        'id': id,
        'name': 'name',
        'image': 'image',
        'price': 0,
        'description': 'description',
    }
    for i in data['orders']:
        if id == i['id']:
            order['id'] = i['id']
            order['name'] = i['name']
            order['price'] = i['price']
            order['image'] = i['image']
            order['description'] = i['description']
    
    return render(request, 'order.html', order)

def sendText(request):
    input_text = request.POST.get('name', 'Проверка подлинности')
    data = {
        'title': 'Услуги',
        'orders': [
            {'id': 1, 
             'name': 'Проверка подлинности',
             'price': 10000,
             'image': "https://mostmag.ru/wp-content/uploads/2020/11/a3028ac6-a555-4a08-9eda-2052f18af329.jpg",
             'description': 'Проверка картины на подлинность. Срок проверки - 3 дня. В срочном порядке - 1 день.'},
            {'id': 2, 
             'name': 'Заказ копии',
             'price': 21000,
             'image': "https://mportret.ru/upload/medialibrary/33a/33af12aefdaa37207355dab3fc2c8afe.png",
             'description': 'Срок создания копии от 7 дней до 3 месяцев в зависимости от размера и техники, в которой выполнена картина.'},
            {'id': 3, 
             'name': 'Определение художника',
             'price': 4200,
             'image': "https://dic.academic.ru/pictures/wiki/files/65/Adriaen_van_Ostade_006.jpg",
             'description': 'Не можете определить чья работа попала к Вам в руки? Мы поможем!'},
            {'id': 4, 
             'name': 'Определение эпохи',
             'price': 3700,
             'image': 'https://yantar.ua/upload/custom/images/0_ac631_dc44a423_orig.jpg',
             'description': 'Определение направления и жанра в котором писал художник. Сроки выполнения 3 - 5 дней.'},
            {'id': 5, 
             'name': 'Реставрация',
             'price': 25000,
             'image': 'https://antiquarika.ru/wp-content/uploads/2021/10/Restavratsiya-kartin.jpg',
             'description': 'Реставрация картин, выполненных маслом.'},
            {'id': 6, 
             'name': 'Заказ на разбор картины',
             'price': 5000,
             'image': "https://s5.afisha.ru/mediastorage/e4/e1/8b1fb0681b304743b342ae72e1e4.jpg",
             'description': 'Не знаете что за картина? Не проблема! Мы поможем узнать все о картине и ее создателе.'},
        ]}
    order = {
        'id': 0,
        'name': 'name',
        'image': 'image',
        'price': 0,
        'description': 'description',
    }
    for i in data['orders']:
        if input_text == i['name']:
            order['id'] = i['id']
            order['name'] = i['name']
            order['price'] = i['price']
            order['image'] = i['image']
            order['description'] = i['description']
    return render(request, 'order.html', order)