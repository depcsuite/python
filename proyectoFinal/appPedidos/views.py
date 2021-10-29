from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import *
from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductoSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



def index(request):

    return HttpResponse(request.encoding)

class CustomAuthToken(ObtainAuthToken):
    
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'uName' : user.username,
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

def verProductos(request):
    data = {}
    context = {}
    data["salida"] = Producto.objects.all()
    context["datos"] = data["salida"]
    return render(request, "listar.html", context)
@login_required
def crearProducto(request):
    if  request.method == "POST":
        
        form = CrearProducto(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
        return HttpResponse(request.encoding)
        
    else:
        context = {}
        context["primerForm"] = CrearProducto()
        return render(request, "form.html", context)


def login_m(request):
    context = {}
    if request.method == "POST":
        logForm = AuthenticationForm(request, data=request.POST)
        uName = logForm.data.get('username')
        uPsswd = logForm.data.get('password')
        user = authenticate(username=uName, password=uPsswd)
        if user != None:
            login(request, user)
            ####     LOGIN CON ÉXITO
            return HttpResponse(request)
        else:
            return HttpResponse(request)
                #####  LOGIN ERRÓNEO
    logForm = AuthenticationForm()
    context["miForm"] = logForm
    return render(request, "form.html", context)


@api_view(["GET"])
def ProductoList(request):
    prods = Producto.objects.all()
    srlz = ProductoSerializer(prods, many=True)
    return Response(srlz.data)

@api_view(["GET"])
def ProductoDet(request, pk):
    
    prods = Producto.objects.get(pk = pk)
    srlz = ProductoSerializer(prods)
    return Response(srlz.data)

class ProductoDetailView(DetailView):
    # specify the model to use
    model = Producto
    template_name ="detalle.html"


class ProductoListView(ListView):
    model = Producto
    template_name = "listar.html"