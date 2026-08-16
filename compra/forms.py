from django import forms
from .models import Proveedor, Producto


class ProveedorForm(forms.ModelForm):
    """Formulario para crear/editar proveedores."""
    
    cuit = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '12345678901',
            'inputmode': 'numeric',
            'pattern': '[0-9]{11}'
        }),
        help_text='Ingresa 11 dígitos sin separadores'
    )
    
    class Meta:
        model = Proveedor
        fields = ['razon_social', 'cuit', 'telefono']
        widgets = {
            'razon_social': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre o razón social del proveedor'
            }),
            'telefono': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1123456789',
                'inputmode': 'tel'
            }),
        }
        labels = {
            'razon_social': 'Razón Social',
            'cuit': 'CUIT',
            'telefono': 'Teléfono (opcional)',
        }
    
    def clean_cuit(self):
        """Valida que el CUIT sea numérico y tenga 11 dígitos."""
        cuit = self.cleaned_data.get('cuit')
        
        if not cuit.isdigit():
            raise forms.ValidationError('El CUIT debe contener solo dígitos.')
        
        if len(cuit) != 11:
            raise forms.ValidationError('El CUIT debe tener exactamente 11 dígitos.')
        
        # Verifica si el CUIT ya existe (excepto en edición)
        if self.instance.pk is None:  # Si es nuevo
            if Proveedor.objects.filter(cuit=int(cuit)).exists():
                raise forms.ValidationError('Este CUIT ya está registrado.')
        
        return int(cuit)


class ProductoForm(forms.ModelForm):
    """Formulario para crear/editar productos."""
    
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'stock_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'precio': 'Precio Unitario ($)',
            'stock_actual': 'Stock Actual',
            'proveedor': 'Proveedor',
        }
    
    def clean_precio(self):
        """Valida que el precio sea positivo."""
        precio = self.cleaned_data.get('precio')
        if precio and precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo.')
        return precio
    
    def clean_stock_actual(self):
        """Valida que el stock sea no negativo."""
        stock = self.cleaned_data.get('stock_actual')
        if stock is not None and stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        return stock