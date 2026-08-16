from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Proveedor(models.Model):
    """Modelo para gestionar proveedores de productos."""
    
    razon_social = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Razón social del proveedor"
    )
    
    cuit = models.BigIntegerField(
        unique=True,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='El CUIT debe tener exactamente 11 dígitos',
                code='invalid_cuit'
            )
        ],
        help_text="CUIT del proveedor (11 dígitos sin separadores)"
    )
    
    telefono = models.BigIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
        help_text="Número de teléfono del proveedor"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación del registro"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha de última actualización"
    )
    
    class Meta:
        ordering = ['razon_social']
        indexes = [
            models.Index(fields=['cuit']),
            models.Index(fields=['razon_social']),
        ]
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    
    def __str__(self):
        return f"{self.razon_social} (CUIT: {self.cuit})"


class Producto(models.Model):
    """Modelo para gestionar productos del inventario."""
    
    nombre = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Nombre del producto"
    )
    
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=False,
        null=False,
        help_text="Precio unitario del producto"
    )
    
    stock_actual = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        help_text="Cantidad disponible en stock"
    )
    
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='productos',
        help_text="Proveedor del producto"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación del registro"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha de última actualización"
    )
    
    class Meta:
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['nombre']),
            models.Index(fields=['proveedor']),
        ]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"