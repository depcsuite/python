from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('verHeaders', views.verHeaders, name='verHeaders'),
    path('saludar', views.saludar, name='saludar'),
    path('verProductos', views.verProductos, name='verProductos'),
    path('productos', views.productos, name='productos'),
    path('marcas', views.marcas, name='marcas'),
    path('herencia', views.verHerencia, name='herencia'),
    path('crearProducto', views.crearProducto, name='crearproducto'),
    path('crearProductoMod', views.crearProductoMod, name='crearproductoMod'),


]
