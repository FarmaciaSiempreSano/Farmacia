from django.db import connections
from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=25)

    class Meta:
        db_table = 'categoria'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=25, unique=True)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    categoria_producto = models.CharField(max_length=35)
    fecha_vencimiento = models.DateField()
    proveedor = models.CharField(max_length=25)
    laboratorio = models.CharField(max_length=25)
    valor_compra = models.FloatField()
    valor_venta = models.FloatField()

    class Meta:
        db_table = 'producto'
        unique_together = [("nombre_producto")]


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    p_nombre = models.CharField(max_length=25)
    a_paterno = models.CharField(max_length=25)
    a_materno = models.CharField(max_length=25)
    nombre_empresa = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=25)
    cp = models.CharField(max_length=25, blank=True, null=True)
    provincia = models.CharField(max_length=25, blank=True, null=True)
    pais = models.CharField(max_length=25)

    class Meta:
        db_table = 'proveedor'