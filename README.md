# Queen_Loans 👑

Aplicación web de gestión de préstamos desarrollada con **Django**, **Python** y **HTML**.

## 📋 Descripción

**Queen_Loans** permite a los clientes solicitar préstamos y a los administradores gestionar préstamos, pagos y categorías de manera eficiente.

## 🎯 Características

- ✅ Gestión de clientes
- ✅ Solicitud y seguimiento de préstamos
- ✅ Registro de pagos
- ✅ Categorización de préstamos
- ✅ Panel de administrador personalizado

## 📊 Modelos y Relaciones

### Modelos Implementados

1. **Cliente** - Información personal de clientes
2. **Préstamo** - Solicitudes de préstamo
3. **Pago** - Registro de pagos realizados
4. **Categoría** - Tipos/categorías de préstamos
5. **Administrador** - Usuarios administradores del sistema

### Relaciones de Base de Datos

```
Cliente (1) ──→ (N) Préstamo
                     ↓
                   Pago (N)
                     
Categoría (N) ←→ (N) Préstamo  [Many-to-Many]

Administrador ←→ Django User [One-to-One]
```

**Relaciones:**
- **Cliente → Préstamo**: Uno a Muchos (1:N)
- **Préstamo → Pago**: Uno a Muchos (1:N)
- **Préstamo ↔ Categoría**: Muchos a Muchos (M:M)
- **Administrador → Usuario**: Uno a Uno (1:1)

## 🗂️ Estructura

```
Queen_Loans/
├── Queen_Loans/
│   ├── loans/
│   │   ├── migrations/
│   │   ├── models.py           # 5 modelos principales
│   │   ├── views.py            # Vistas de la aplicación
│   │   ├── urls.py             # Rutas
│   │   ├── forms.py            # Formularios
│   │   ├── admin.py            # Panel administrativo
│   │   └── tests.py
│   ├── Queen_Loans/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── templates/
│   ├── manage.py
│   └── db.sqlite3
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Instalación

### Requisitos
- Python 3.8+
- pip

### Pasos

```bash
# Clonar repositorio
git clone https://github.com/carolina899/Queen_Loans.git
cd Queen_Loans

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

## 🌐 Acceso

- **Aplicación**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/

## 📚 Tecnologías

| Tecnología | Versión |
|-----------|---------|
| Django | 5.2+ |
| Python | 3.8+ |
| SQLite | - |
| HTML | 5 |
| CSS | 3 |

## 🔐 Funcionalidades del Admin

El panel administrativo permite:

- **CRUD de Clientes**: Crear, ver, editar y eliminar clientes
- **CRUD de Préstamos**: Gestionar préstamos y sus categorías
- **CRUD de Pagos**: Registrar y visualizar pagos
- **CRUD de Categorías**: Crear y gestionar categorías de préstamos
- **Filtros avanzados**: Buscar por estado, fecha, cliente, etc.
- **Visualización de relaciones**: Ver préstamos por cliente, pagos por préstamo, categorías asignadas

## 📋 Ejemplos de Uso

### Crear un préstamo con categorías

```python
# Desde Django shell
from loans.models import Cliente, Prestamo, Categoria

cliente = Cliente.objects.get(id=1)
prestamo = Prestamo.objects.create(
    cliente=cliente,
    monto=5000.00,
    tasa_interes=5.5,
    fecha_vencimiento='2026-12-31',
    estado='pendiente'
)

# Asignar categorías (Many-to-Many)
categoria1 = Categoria.objects.get(nombre='Personal')
categoria2 = Categoria.objects.get(nombre='Educativo')
prestamo.categorias.add(categoria1, categoria2)
```

### Registrar un pago

```python
from loans.models import Pago

pago = Pago.objects.create(
    prestamo=prestamo,
    monto_pagado=1000.00,
    metodo_pago='transferencia'
)
```

## 👤 Autor

**Carolina**  
GitHub: [@carolina899](https://github.com/carolina899)

## 📄 Licencia

MIT License
