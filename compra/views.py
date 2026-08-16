from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm


# ==================== VISTAS PROVEEDOR ====================

class ProveedorListView(ListView):
    """Vista para listar todos los proveedores con búsqueda."""
    model = Proveedor
    template_name = 'compra/listar_proveedores.html'
    context_object_name = 'proveedores'
    paginate_by = 20
    
    def get_queryset(self):
        """Obtiene queryset ordenado y filtrado por búsqueda."""
        queryset = super().get_queryset().order_by('razon_social')
        
        # Búsqueda por razón social o CUIT
        busqueda = self.request.GET.get('busqueda', '')
        if busqueda:
            queryset = queryset.filter(
                Q(razon_social__icontains=busqueda) |
                Q(cuit__icontains=busqueda)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Agrega datos adicionales al contexto."""
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('busqueda', '')
        context['total_proveedores'] = self.get_queryset().count()
        return context


class ProveedorCreateView(SuccessMessageMixin, CreateView):
    """Vista para crear un nuevo proveedor."""
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'compra/agregar_proveedor.html'
    success_url = reverse_lazy('compra:listar_proveedores')
    success_message = 'Proveedor "%(razon_social)s" agregado correctamente.'
    
    def get_context_data(self, **kwargs):
        """Agrega título al contexto."""
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Proveedor'
        return context


class ProveedorUpdateView(SuccessMessageMixin, UpdateView):
    """Vista para editar un proveedor existente."""
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'compra/agregar_proveedor.html'
    success_url = reverse_lazy('compra:listar_proveedores')
    success_message = 'Proveedor "%(razon_social)s" actualizado correctamente.'
    
    def get_context_data(self, **kwargs):
        """Agrega título al contexto."""
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Proveedor'
        return context


class ProveedorDeleteView(SuccessMessageMixin, DeleteView):
    """Vista para eliminar un proveedor."""
    model = Proveedor
    template_name = 'compra/confirmar_eliminar_proveedor.html'
    success_url = reverse_lazy('compra:listar_proveedores')
    success_message = 'Proveedor eliminado correctamente.'
    
    def delete(self, request, *args, **kwargs):
        """Agrega mensaje de éxito al eliminar."""
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)


# ==================== VISTAS PRODUCTO ====================

class ProductoListView(ListView):
    """Vista para listar todos los productos con búsqueda, filtros y ordenamiento."""
    model = Producto
    template_name = 'compra/listar_productos.html'
    context_object_name = 'productos'
    paginate_by = 20
    
    def get_queryset(self):
        """Obtiene queryset con búsqueda, filtro y ordenamiento."""
        queryset = super().get_queryset().select_related('proveedor')
        
        # Búsqueda por nombre o proveedor
        busqueda = self.request.GET.get('busqueda', '')
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(proveedor__razon_social__icontains=busqueda)
            )
        
        # Filtrado por proveedor
        proveedor_id = self.request.GET.get('proveedor')
        if proveedor_id:
            queryset = queryset.filter(proveedor_id=proveedor_id)
        
        # Ordenamiento (por defecto: nombre)
        orden = self.request.GET.get('orden', 'nombre')
        queryset = queryset.order_by(orden)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Agrega datos adicionales al contexto."""
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['busqueda'] = self.request.GET.get('busqueda', '')
        context['proveedor_seleccionado'] = self.request.GET.get('proveedor')
        context['total_productos'] = self.get_queryset().count()
        return context


class ProductoCreateView(SuccessMessageMixin, CreateView):
    """Vista para crear un nuevo producto."""
    model = Producto
    form_class = ProductoForm
    template_name = 'compra/agregar_producto.html'
    success_url = reverse_lazy('compra:listar_productos')
    success_message = 'Producto "%(nombre)s" agregado correctamente.'
    
    def get_context_data(self, **kwargs):
        """Agrega título al contexto."""
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Agregar Producto'
        return context


class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    """Vista para editar un producto existente."""
    model = Producto
    form_class = ProductoForm
    template_name = 'compra/agregar_producto.html'
    success_url = reverse_lazy('compra:listar_productos')
    success_message = 'Producto "%(nombre)s" actualizado correctamente.'
    
    def get_context_data(self, **kwargs):
        """Agrega título al contexto."""
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Producto'
        return context


class ProductoDeleteView(SuccessMessageMixin, DeleteView):
    """Vista para eliminar un producto."""
    model = Producto
    template_name = 'compra/confirmar_eliminar_producto.html'
    success_url = reverse_lazy('compra:listar_productos')
    success_message = 'Producto eliminado correctamente.'
    
    def delete(self, request, *args, **kwargs):
        """Agrega mensaje de éxito al eliminar."""
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)