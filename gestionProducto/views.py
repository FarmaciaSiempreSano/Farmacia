from django.shortcuts import render
from django.contrib import messages
from gestionProducto.models import Producto
from gestionProducto.models import Categoria
from gestionProducto.models import Proveedor
# Create your views here.

def Productorecord(request):
    results=Categoria.objects.all()
    results2=Proveedor.objects.all()
    results3=Producto.objects.all()
    if request.method=="POST":
        if request.POST.get('nombre_producto') and request.POST.get('stock') and request.POST.get('categoria_producto') and request.POST.get('fecha_vencimiento') and request.POST.get('proveedor') and request.POST.get('laboratorio') and request.POST.get('valor_compra') and request.POST.get('valor_venta') and request.POST.get('descripcion'):
            saverecord=Producto()
            saverecord.nombre_producto=request.POST.get('nombre_producto')
            saverecord.stock=request.POST.get('stock')
            saverecord.categoria_producto=request.POST.get('categoria_producto')
            saverecord.fecha_vencimiento=request.POST.get('fecha_vencimiento')
            saverecord.proveedor=request.POST.get('proveedor')
            saverecord.laboratorio=request.POST.get('laboratorio')
            saverecord.valor_compra=request.POST.get('valor_compra')
            saverecord.valor_venta=request.POST.get('valor_venta')
            saverecord.descripcion=request.POST.get('descripcion')
            saverecord.save()
            messages.success(request,'PRODUCTO AÑADIDO CORRECTAMENTE')
            return render(request,'registro_productos.html',{'Categoria':results, 'Proveedor':results2,'Producto':results3})       
    else:
            return render(request,'registro_productos.html',{'Categoria':results, 'Proveedor':results2,'Producto':results3})
