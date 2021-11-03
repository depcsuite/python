from django.shortcuts import render
from django.http import HttpResponse
from appuno.models import Marca, Producto
from .forms import *
def index(request):
    #parametrosGet = request.GET["dato"]
    #return HttpResponse("Pasamos como parámetro... " + parametrosGet)
    return HttpResponse("Pasamos como parámetro... ")
def verHeaders(request):
    hds = request.META
    return HttpResponse(hds)
def saludar(request):
    return HttpResponse("Un saludo...   ")
def verProductos(request):
    data = {}
    data["dataset"] = Producto.objects.all()
    out = ""
    for prod in data["dataset"]:
        out = out+str(prod) #Aprovechamos __str()__
    return HttpResponse(out)#Retornamos la concatenación
def productos(request):
    data = {}
    context = {}
    data["salida"] = Producto.objects.all()
    context["datos"] = data["salida"]
    return render(request, "detalle.html", context)
def marcas(request):
    data = {}
    context = {}
    data["salida"] = Marca.objects.all()
    context["datos"] = data["salida"]
    return render(request, "detalleMarcas.html", context)
def verHerencia(request):
    data = {}
    context = {}
    data["salida"] = Marca.objects.all()
    context["datos"] = data["salida"]
    return render(request, "seccionUno.html", context)
def crearProducto(request):
    context = {}
    context["primerForm"] = CrearProducto()
    return render(request, "form.html", context)
def crearProductoMod(request):
    if request.method == "POST":
        form = CrearProductoPro(request.POST)
        form.save(commit=True)
    else:
        context = {}
        context["primerForm"] = CrearProductoPro()
        return render(request, "form.html", context)
