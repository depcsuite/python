from django.shortcuts import render
from django.http import HttpResponse
from appuno.models import Marca, Producto
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import authenticate
from .forms import *
from django.contrib.auth.decorators import *
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
def productoDet(request,id=None):
    data = {}
    data["salida"] = Producto.objects.filter(id=id)
    context = {}
    context["datos"] = data["salida"]
    #return HttpResponse(context["datos"])
    return render(request, "detalleP.html", context)
def marcaDet(request,id=None):
    data = {}
    data["salida"] = Marca.objects.filter(id=id)
    context = {}
    context["datos"] = data["salida"]
    return render(request, "detalleP.html", context)
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
#@login_required
def crearProductoMod(request):
    if request.method == "POST":
        form = CrearProductoPro(request.POST, request.FILES)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponse("Exito")
        else:
            return HttpResponse("Error")
    else:
        context = {}
        context["primerForm"] = CrearProductoPro()
        return render(request, "form.html", context)
def crearMarca(request):
    if request.method == "POST":
        form = CrearMarcaPro(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponse("Exito")
        else:
            return HttpResponse("Error")
    else:
        context = {}
        context["formMarca"] = CrearMarcaPro()
        return render(request, "formMarca.html", context)
def modificarProducto(request, id):
    context = {}
    prod = Producto.objects.filter(id=id).first()
    form = CrearProductoPro(request.POST or None, instance=prod)
    context["miForm"] = form
    return render(request, "form.html", context)




def loginUser(request, user=None):
    context = {}
    if request.method == "POST":
        logForm = AuthenticationForm(request, data=request.POST)
        uName = logForm.data.get('username')
        uPsswd = logForm.data.get('password')
        user = authenticate(username=uName, password=uPsswd)
        if user != None:
            loginUser(request, user)
            ####     LOGIN CON ÉXITO
            return HttpResponse("Exito")
        else:
            return HttpResponse("Error")
                #####  LOGIN ERRÓNEO
    logForm = AuthenticationForm()
    context["miForm"] = logForm
    return render(request, "form.html", context)


