from django.contrib import admin
from .models import Proveedor, Producto
   
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['razon_social', 'cuit', 'telefono', 'created_at']
    search_fields = ['razon_social', 'cuit']
    ordering = ['-created_at']
   
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock_actual', 'proveedor']
    search_fields = ['nombre', 'proveedor__razon_social']
    list_filter = ['proveedor', 'created_at']