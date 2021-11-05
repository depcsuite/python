from django.contrib import admin

from appPedidos.models import Marca, ProductoPedido, Producto, Pedido

# Register your models here.
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ProductoPedido)
admin.site.register(Marca)