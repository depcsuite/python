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
    path('detProducto/<id>', views.productoDet, name='productoDet'),
    path('detMarca/<id>', views.marcaDet, name='marcaDet'),
    path('crearProductoMod', views.crearProductoMod, name='crearproductoMod'),
    path('modProd/<id>', views.modificarProducto, name='modificarproducto'),
    path('crearMarca', views.crearMarca, name='crearMarca'),
    path('loginus', views.loginUser, name='loginUser'),


]
