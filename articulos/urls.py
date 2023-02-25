from django.contrib import admin
from django.urls import path
from .views import ArticuloView , eliminarArticulo,crearArticulo,editarArticulo,guardarArticulo
from django.views import *

urlpatterns = [
    path('', ArticuloView.as_view(),name='all'),
    path('eliminar/<id>', eliminarArticulo, name='eliminar'),
    path('crear/',crearArticulo,name='crear'),
    path('editar/<id>',editarArticulo,name='editar'),
    path('guardar/<id>',guardarArticulo,name='guardar'),
]
