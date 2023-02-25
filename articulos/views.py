from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Articulo

class ArticuloView(ListView):
    model = Articulo
    template_name = "index.html"

def eliminarArticulo(request,id):
    print("la id es",id)
    articulo=Articulo.objects.get(id=id)
    articulo.delete()
    return redirect('/')

def crearArticulo(request):
    nombre=request.POST["nombre"]
    stock=request.POST["stock"]
    precio=request.POST["precio"]
    articulo=Articulo(nombre=nombre,stock=stock,precio=precio)
    articulo.save()
    return redirect("/")

def editarArticulo(request,id):
    articulo=Articulo.objects.get(id=id)
    return render( request, 'editar.html', {'articulo': articulo})

def guardarArticulo(request,id):
    articulo=Articulo.objects.get(id=id)
    articulo.nombre=request.POST["nombre"]
    articulo.precio=request.POST["precio"]
    articulo.stock=request.POST["stock"]
    articulo.save()
    return redirect ("/")


# Create your views here.


