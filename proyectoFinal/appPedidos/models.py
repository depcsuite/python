from django.db import models
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    class Meta:
        db_table="appPedidos_marca"
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img')
    def __str__(self):
        return self.nombre
class Pedido(models.Model):
    fecha = models.DateField()
    productosPedidos = models.ManyToManyField(Producto, through='ProductoPedido')
    estado = models.CharField(choices=[('E','ENTREGADO'),('P','PENDIENTE'),('V','EN VIAJE')], \
    max_length=1, default='P')
    class Meta:
        db_table="appPedidos_pedido"
class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    class Meta:
        db_table="appPedidos_productopedido"