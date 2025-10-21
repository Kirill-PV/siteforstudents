from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Лекции и материалы", 'url_name': 'materials'},
        {'title':"Добавить лекцию или учебник", 'url_name': 'add_material'},
        {'title': "Войти", 'url_name': 'login'}
        ]
#        {'title': "Студентам", 'url_name': 'students'},
#



def index(request):
    context = {'menu': menu,
               'title': 'Главная страница'}
    return render(request, 'homepage/index.html', context=context)

def about(request):
    return render(request, 'homepage/about.html', {'menu': menu, 'title': 'О сайте'})

def add_materials(request):
    return HttpResponse('Добавление лекции')

def materials(request):
    return HttpResponse('Лекции')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_material(request, material_id):
    return HttpResponse(f'Отображение материала с id = {material_id}')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')