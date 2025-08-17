from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Страница приложения Homepage')

def categories(request, cat):
    return HttpResponse(f'<h1>Категории приложения Homepage</h1><p>{cat}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')