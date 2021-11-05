from django.db import models
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    class Meta:
        db_table="appPedidos_marca"
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img')
    class Meta:
        db_table="appPedidos_producto"
    def __str__(self):
        return self.nombre + self.descripcion