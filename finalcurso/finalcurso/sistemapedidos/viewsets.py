import rest_framework
from rest_framework import viewsets
from sistemapedidos import models
from sistemapedidos.models import Marca, Pedido, Producto, ProductoPedido
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
class ProductoViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProductoSerializer
    queryset = Producto.objects.all()
class MarcaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = Marca.objects.all()
class PedidoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PedidoSerializer
    queryset = Pedido.objects.all()
    @action(detail=True, methods=['GET'], name='Lista por cliente')
    def c(self, request, pk=None):
        queryset = models.Pedido.objects.filter(cliente=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class ProductoPedidoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductoPedidoSerializer
    queryset = ProductoPedido.objects.all()
    @action(detail=True, methods=['GET'], name='Detalle validado')
    def det(self, request, pk=None):
        queryset = models.ProductoPedido.objects.filter(pedido=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)