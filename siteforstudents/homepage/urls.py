from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/homepage/
    path('about/', about, name='about'),
    path('addmaterial/', add_materials, name='add_material'),
    path('contact/', contact, name='contact'),
    path('materials/', materials, name='materials'),
    path('login/', login, name='login'),
    path('material/<int:material_id>/', show_material, name='show_material'),



]