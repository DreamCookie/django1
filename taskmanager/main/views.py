from django.shortcuts import render
from .models import Task



def index(requests):
    tasks = Task.objects.all()
    return render(requests, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(requests):
    return render(requests, 'main/about.html')

