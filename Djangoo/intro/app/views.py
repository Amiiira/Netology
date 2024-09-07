from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    msg = f'Текущее время: {datetime.datetime.now()}'
    return HttpResponse(msg)


def workdir_view(request):
    current_directory = os.getcwd()
    all_items = os.listdir(current_directory)
    files = [item + ' ' for item in all_items if os.path.isfile(os.path.join(current_directory, item))]
    return HttpResponse(files)
