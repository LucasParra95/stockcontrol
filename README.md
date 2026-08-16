# StockControl

Sistema de gestión de inventario desarrollado con **Django** para administrar productos y proveedores de forma centralizada. Proyecto realizado como tarea del curso de Backend con Django de la Secretaría de Energía de Río Negro en colaboración con Alkemy.

## 📋 ¿Qué es StockControl?

StockControl es una aplicación web que permite:

- Registrar y gestionar proveedores con su información de contacto
- Administrar productos del inventario
- Buscar y filtrar productos por nombre o proveedor
- Ordenar productos por precio, nombre o cantidad en stock
- Visualizar el estado del inventario con indicadores de stock bajo
- Realizar operaciones de crear y listar proveedores y productos

## ✨ Características Principales

- **Gestión de Proveedores**
  - Crear, editar y eliminar proveedores
  - Validación de CUIT (11 dígitos)
  - Teléfono opcional
  - Búsqueda por razón social o CUIT

- **Gestión de Productos**
  - Crear productos
  - Asignar proveedor a cada producto
  - Control de precio y cantidad en stock
  - Validación de valores no-negativos

- **Búsqueda y Filtrado**
  - Búsqueda por nombre de producto o proveedor
  - Filtrado por proveedor específico
  - Ordenamiento por nombre, precio o stock

- **Indicadores Visuales**
  - Stock alto (>30): Verde
  - Stock medio (11-30): Amarillo
  - Stock bajo (≤10): Rojo

- **Interfaz Responsiva**
  - Diseño moderno con Bootstrap 5
  - Navegación intuitiva
  - Compatible con móviles y escritorio
  - Mensajes de confirmación para todas las acciones

## 🔧 Requisitos Previos

- **Python:** 3.8 o superior
- **pip:** Gestor de paquetes de Python
- **Django:** 4.0 o superior
- **Navegador moderno:** Chrome, Firefox, Safari o Edge (última versión)

## 🚀 Instrucciones de Inicio

### 1. Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual
# En Windows:
env\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install Django
```

### 3. Aplicar Migraciones

```bash
python manage.py migrate
```

### 4. Crear Superusuario (Admin)

```bash
python manage.py createsuperuser
```

Ingresa:
- Nombre de usuario
- Email
- Contraseña (2 veces)

### 5. Ejecutar Servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en:

- **Frontend:** http://localhost:8000/compra/productos/
- **Panel Admin:** http://localhost:8000/admin/

## 📱 Cómo Usar la Aplicación

### Agregar un Proveedor

1. Hacer clic en "Nuevo Proveedor" desde la navbar
2. Completar el formulario:
   - **Razón Social:** Nombre del proveedor
   - **CUIT:** 11 dígitos (sin separadores)
   - **Teléfono:** Opcional
3. Hacer clic en "Guardar Proveedor"

### Agregar un Producto

1. Hacer clic en "Nuevo Producto" desde la navbar
2. Completar el formulario:
   - **Nombre:** Nombre del producto
   - **Precio:** Valor unitario
   - **Stock Actual:** Cantidad disponible
   - **Proveedor:** Seleccionar de la lista
3. Hacer clic en "Guardar Producto"

### Buscar Productos

1. Ir a "Productos" desde la navbar
2. Usar el campo de búsqueda para filtrar por:
   - Nombre del producto
   - Razón social del proveedor
3. Opcional: Filtrar por proveedor específico o cambiar orden


## 📊 Estructura de Datos

### Modelo: Proveedor

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Razón Social | Texto | Nombre del proveedor |
| CUIT | Número | 11 dígitos únicos |
| Teléfono | Número | Contacto (opcional) |

### Modelo: Producto

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Nombre | Texto | Nombre del producto |
| Precio | Decimal | Precio unitario |
| Stock Actual | Número | Cantidad disponible |
| Proveedor | Referencia | FK al proveedor |

## 🔗 Rutas Disponibles

```
/compras/productos/listado/           - Listar 
productos

/compras/productos/crear/             - Crear producto


/compras/proveedores/listado/         - Listar proveedores

/compras/proveedores/crear/           - Crear proveedor

/admin/                               - Panel de administración
```

## 🛡️ Validaciones

- **CUIT:** Debe tener exactamente 11 dígitos y ser único
- **Precio:** No puede ser negativo
- **Stock:** No puede ser negativo
- **Razón Social:** Campo requerido
- **Nombre de Producto:** Campo requerido
- **Proveedor:** Debe ser seleccionado para crear producto

## 💾 Base de Datos

Por defecto, StockControl utiliza **SQLite** (db.sqlite3), ideal para desarrollo. 

Para producción, se recomienda usar **PostgreSQL** o **MySQL**. Modificar `settings.py` según sea necesario.

## 📝 Notas Importantes

- **on_delete=PROTECT:** No se puede eliminar un proveedor si tiene productos asociados
- **Búsqueda case-insensitive:** La búsqueda no diferencia entre mayúsculas y minúsculas
- **Paginación:** Se muestran 20 registros por página
- **Timestamps:** Todos los registros incluyen fecha de creación y última actualización

## 🐛 Troubleshooting

### Error: "No migrations detected in app 'compra'"

```bash
python manage.py makemigrations compra
python manage.py migrate
```

### Error: "ModuleNotFoundError: No module named 'compra'"

Verificar que `'compra'` está en `INSTALLED_APPS` en `settings.py`.

### Error: CUIT rechazado

Asegurar que sean exactamente 11 dígitos sin separadores (ej: 20123456789).

## 🔄 Próximas Mejoras Planeadas

- Historial de cambios en inventario
- Reportes y estadísticas
- Gestión de pedidos a proveedores
- Sistema de usuarios y permisos
- API REST
- Exportación a PDF/Excel

