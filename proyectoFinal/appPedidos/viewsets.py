from rest_framework import viewsets
import rest_framework
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from djoser import *
from rest_framework import viewsets
import rest_framework
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from djoser import *
class ProductoViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    @action(detail=True, methods=['post'])
    def prueba(self, request):  
        queryset = models.Producto.objects.all()    
        serializer = serializers.ProductoSerializer(queryset, many=True)
        return Response(serializer.data)     
    def update(self, request, pk=None):
        serializer = serializers.ProductoSerializer(data=request.data)
        if serializer.is_valid():
            models.Producto.objects.filter(id=pk).  update(**serializer.data)
        return Response(serializer.validated_data)


    def list(self, request):
        queryset = models.Producto.objects.all()
        serializer = serializers.ProductoSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        queryset = models.Producto.objects.filter(id=pk)
        serializer = serializers.ProductoSerializer(queryset, many=True)
        return Response(serializer.data)
    def destroy(self, request, pk):
        models.Producto.objects.filter(id=pk).delete()
        return Response(request.data)
    def partial_update(self, request):
        serializer = serializers.ProductoSerializer(data=request.data)
        if serializer.is_valid():
            models.Producto.objects.create(**serializer.data)

            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },)
    def create(self, request):
        serializer = serializers.ProductoSerializer(data=request.data)
        if serializer.is_valid():
            models.Producto.objects.create(**serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },) 

class PedidoViewset(viewsets.ViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    @action(detail=True, methods=['post'])
    def prueba(self, request):  
        queryset = models.Producto.objects.all()    
        serializer = serializers.ProductoSerializer(queryset, many=True)
        return Response(serializer.data)     
    def update(self, request, pk=None):
        serializer = serializers.PedidoSerializer(data=request.data)
        if serializer.is_valid():
            models.Pedido.objects.filter(id=pk).update(serializer.data)
        return Response(serializer.validated_data)
    def list(self, request):
        queryset = models.Pedido.objects.all()
        serializer = serializers.PedidoSerializer(queryset, many=True)
        return Response(serializer .data)
    def retrieve(self, request, pk):
        queryset = models.Pedido.objects.filter(id=pk)
        serializer = serializers.PedidoSerializer(queryset, many=True)
        return Response(serializer.data)
    def destroy(self, request, pk):
        models.Pedido.objects.filter(id=pk).delete()
        return Response(request.data)
    def partial_update(self, request):
        serializer = serializers.PedidoSerializer(data=request.data)
        if serializer.is_valid():
            models.Pedido.objects.create(serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },)
    def create(self, request):
        serializer = serializers.PedidoSerializer(data=request.data)
        if serializer.is_valid():
            models.Pedido.objects.create(serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },) 
class MarcaViewset(viewsets.ViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    @action(detail=True, methods=['post'])
    def prueba(self, request):  
        queryset = models.Marca.objects.all()    
        serializer = serializers.MarcaSerializer(queryset, many=True)
        return Response(serializer.data)     
    def update(self, request, pk=None):
        serializer = serializers.MarcaSerializer(data=request.data)
        if serializer.is_valid():
            models.Marca.objects.filter(id=pk).update(serializer.data)
        return Response(serializer.validated_data)
    def list(self, request):
        queryset = models.Marca.objects.all()
        serializer = serializers.MarcaSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        queryset = models.Marca.objects.filter(id=pk)
        serializer = serializers.MarcaSerializer(queryset, many=True)
        return Response(serializer.data)
    def destroy(self, request, pk):
        models.Marca.objects.filter(id=pk).delete()
        return Response(request.data)
    def partial_update(self, request):
        serializer = serializers.MarcaSerializer(data=request.data)
        if serializer.is_valid():
            models.Marca.objects.create(serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },)
    def create(self, request):
        serializer = serializers.MarcaSerializer(data=request.data)
        if serializer.is_valid():
            models.Marca.objects.create(serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },) 
class ProductoPedidoViewset(viewsets.ViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    @action(detail=True, methods=['post'])
    def prueba(self, request):  
        queryset = models.ProductoPedido.objects.all()    
        serializer = serializers.MarcaSerializer(queryset, many=True)
        return Response(serializer.data)     
    def update(self, request, pk=None):
        serializer = serializers.ProductoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            models.ProductoPedido.objects.filter(id=pk).update(serializer.data)
        return Response(serializer.validated_data)
    def list(self, request):
        queryset = models.ProductoPedido.objects.all()
        serializer = serializers.ProductoPedidoSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        queryset = models.ProductoPedido.objects.filter(id=pk)
        serializer = serializers.ProductoPedidoSerializer(queryset, many=True)
        return Response(serializer.data)
    def destroy(self, request, pk):
        models.ProductoPedido.objects.filter(id=pk).delete()
        return Response(request.data)
    def partial_update(self, request):
        serializer = serializers.ProductoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            models.ProductoPedido.objects.create(serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },)
    def create(self, request):
        serializer = serializers.MarcaSerializer(data=request.data)
        if serializer.is_valid():
            models.Marca.objects.create(serializer.data)
            return Response(serializer.validated_data)
        
        return Response({
            'message': 'Error, request incompleto'
        },) 