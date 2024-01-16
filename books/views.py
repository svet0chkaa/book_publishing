from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import re
import logging

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })

def GetWorks(request):
    pattern = request.GET.get('wrk')
    data = GetData(0)
    
    if pattern:
        data['collection']['input_value'] = pattern
        result_of_search = []
        for i in data['collection']['workrs']:
            if re.search(pattern, i['title']):
                result_of_search.append(i)

        data['collection']['works'] = result_of_search

    return render(request, 'works.html', data)

def GetWork(request, id):
    data = GetData(id)
    return render(request, 'work.html', {'data': data
    })

def GetData(id):
    data = {'collection' : {
        'current_date': date.today(),
        'works': [
            {'title': 'Печать', 'id': 1, 'price': "От 10 руб. за 1 страницу", "img": "img/1.jpg", "description" : "Для уточнения деталей услуги свяжитесь с нами."},
            {'title': 'Брошюрирование', 'id': 2, 'price': "От 500 руб.", "img": "img/2.jpg", "description": "Для уточнения деталей услуги свяжитесь с нами."},
            {'title': 'Дизайн обложки', 'id': 3, 'price': "От 1500 руб.", "img": "img/3.jpg", "description": "Создадим уникальный дизайн обложки для Вас! Для уточнения деталей услуги свяжитесь с нами."},
            {'title': 'Подарок', 'id': 4, 'price': "От 1000 руб.", "img": "img/4.jpg", "description": "Порадуйте себя или близких!"},
        ],
    'input_value' : ''
    }}
    if id == 0:
        return data
    else:
        for i in data['collection']['workrs']:
            if i['id'] == id:
                return i
    return -1
    
# Create your views here.
