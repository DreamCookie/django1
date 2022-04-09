from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(requests):
    return render(requests, 'main/index.html')

def about(requests):
    return render(requests, 'main/about.html')

