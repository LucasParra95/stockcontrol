from django.urls import path
from . import views

app_name = 'compra'

urlpatterns = [
    # Proveedores
    path('proveedores/crear/', views.ProveedorCreateView.as_view(), name='agregar_proveedor'),
    path('proveedores/listado/', views.ProveedorListView.as_view(), name='listar_proveedores'),
    
    # Productos
    path('productos/crear/', views.ProductoCreateView.as_view(), name='agregar_producto'),
    path('productos/listado/', views.ProductoListView.as_view(), name='listar_productos'),
]