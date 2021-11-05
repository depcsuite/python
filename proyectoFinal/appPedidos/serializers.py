from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer): #Remarcar este gran peligro
    class Meta:
        model = Producto
        fields = "__all__"
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
class ProductoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPedido
        fields = "__all__"