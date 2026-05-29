# Queen_Loans 👑

## 📋 Descripción del Proyecto

**Queen_Loans** es una aplicación web de gestión de préstamos desarrollada con **Django**, **Java** y **HTML**. Esta plataforma permite a los clientes solicitar préstamos y a los administradores gestionar y hacer seguimiento de los mismos, incluyendo pagos y control de estados.

---

## 🎯 Funcionalidades Principales

### 👥 Gestión de Clientes
- Registrar nuevos clientes con información personal
- Almacenar datos de contacto (email, teléfono, dirección)
- Mantener historial de fecha de registro y nacimiento
- Visualizar perfil de cliente

### 💰 Gestión de Préstamos
- Crear solicitudes de préstamo con monto específico
- Definir tasa de interés anual
- Establecer fechas de inicio y vencimiento
- Rastrear estado del préstamo (Pendiente, Pagado, Atrasado)
- Consultar préstamos activos y completados

### 💳 Registro de Pagos
- Registrar pagos asociados a préstamos
- Múltiples métodos de pago (Efectivo, Transferencia, Tarjeta)
- Rastreo de fecha y monto pagado
- Historial completo de pagos por préstamo

### 🔐 Administración
- Panel de administrador con acceso a todas las funciones
- Control de usuarios del sistema
- Gestión completa de datos

---

## 📊 Arquitectura y Relaciones de Base de Datos

### Diagrama de Relaciones

```
┌─────────────────┐          ┌──────────────────┐          ┌────────────┐
│    CLIENTE      │          │    PRESTAMO      │          │    PAGO    │
├─────────────────┤          ├──────────────────┤          ├────────────┤
│ • id (PK)       │◄─────┐   │ • id (PK)        │◄─────┐   │ • id (PK)  │
│ • nombre        │  1:N  ├──│ • cliente_id (FK)│  1:N  ├──│ • prestamo │
│ • apellido      │       │   │ • monto          │       │   │   _id (FK) │
│ • email         │       │   │ • tasa_interes   │       │   │ • fecha    │
│ • telefono      │       │   │ • fecha_inicio   │       │   │ • monto    │
│ • direccion     │       │   │ • fecha_vencim.  │       │   │ • método   │
│ • fecha_registro│       │   │ • estado         │       │   └────────────┘
│ • fecha_nacim.  │       │   └──────────────────┘       │
└─────────────────┘       │                              │
                          └──────────────────────────────┘

┌──────────────────┐
│  ADMINISTRADOR   │
├──────────────────┤
│ • id (PK)        │
│ • usuario (FK)   │───────► Django User
│ • telefono       │
└──────────────────┘
```

### Descripción de Relaciones

#### 1️⃣ **Relación Cliente → Préstamo (Uno a Muchos)**
```
Cliente (1) ────────> (N) Préstamo
```
- Un cliente puede tener **múltiples préstamos**
- Cada préstamo pertenece a **un solo cliente**
- **Relación**: `ForeignKey(Cliente)`
- **Cascada**: Si se elimina un cliente, se eliminan todos sus préstamos

#### 2️⃣ **Relación Préstamo → Pago (Uno a Muchos)**
```
Préstamo (1) ────────> (N) Pago
```
- Un préstamo puede tener **múltiples pagos**
- Cada pago corresponde a **un solo préstamo**
- **Relación**: `ForeignKey(Prestamo)`
- **Cascada**: Si se elimina un préstamo, se eliminan todos sus pagos

#### 3️⃣ **Relación Administrador → Usuario (Uno a Uno)**
```
Administrador (1) ◄────► (1) Django User
```
- Un administrador corresponde a **un solo usuario** del sistema
- Cada usuario administrador tiene **un único registro** de administrador
- **Relación**: `OneToOneField(User)`

---

## 🗂️ Estructura del Proyecto

```
Queen_Loans/
├── Queen_Loans/                 # Carpeta principal del proyecto Django
│   ├── loans/                   # Aplicación Django de préstamos
│   │   ├── migrations/          # Migraciones de base de datos
│   │   ├── models.py            # Modelos de datos (Cliente, Préstamo, Pago, Administrador)
│   │   ├── views.py             # Vistas de la aplicación
│   │   ├── urls.py              # Rutas de la aplicación
│   │   ├── forms.py             # Formularios de Django
│   │   ├── admin.py             # Configuración de admin de Django
│   │   └── tests.py             # Pruebas unitarias
│   ├── Queen_Loans/             # Carpeta de configuración del proyecto
│   │   ├── settings.py          # Configuración general
│   │   ├── urls.py              # Rutas principales
│   │   ├── wsgi.py              # Configuración WSGI
│   │   └── asgi.py              # Configuración ASGI
│   ├── manage.py                # Script de gestión de Django
│   ├── db.sqlite3               # Base de datos (desarrollo)
│   └── templates/               # Plantillas HTML
│       ├── base.html            # Plantilla base
│       ├── cliente/             # Plantillas de clientes
│       ├── prestamo/            # Plantillas de préstamos
│       └── pago/                # Plantillas de pagos
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias de Python
└── .gitignore                   # Archivos a ignorar en Git
```

---

## 📦 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| **Django** | 5.2+ | Framework web backend |
| **Python** | 3.8+ | Lenguaje de programación |
| **Django ORM** | - | Gestión de base de datos |
| **HTML** | 5 | Maquetación frontend |
| **CSS** | 3 | Estilos y diseño |
| **SQLite** | - | Base de datos (desarrollo) |
| **Java** | 8+ | (Especificar función) |

---

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/carolina899/Queen_Loans.git
cd Queen_Loans
```

2. **Crear un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones de base de datos**
```bash
python manage.py migrate
```

5. **Crear un superusuario (administrador)**
```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Aplicación: http://localhost:8000/
- Admin: http://localhost:8000/admin/

---

## 📚 Modelos de Datos

### Modelo Cliente
```python
class Cliente(models.Model):
    nombre              # CharField(max_length=100)
    apellido            # CharField(max_length=100)
    email               # EmailField(unique=True)
    telefono            # CharField(max_length=15)
    direccion           # TextField
    fecha_registro      # DateTimeField(auto_now_add=True)
    fecha_nacimiento    # DateField
```

### Modelo Préstamo
```python
class Prestamo(models.Model):
    cliente             # ForeignKey(Cliente) → Relación 1:N
    monto               # DecimalField(max_digits=10, decimal_places=2)
    tasa_interes        # DecimalField(porcentaje anual)
    fecha_inicio        # DateField
    fecha_vencimiento   # DateField
    estado              # CharField(choices=['pendiente', 'pagado', 'atrasado'])
```

### Modelo Pago
```python
class Pago(models.Model):
    prestamo            # ForeignKey(Prestamo) → Relación 1:N
    fecha_pago          # DateTimeField
    monto_pagado        # DecimalField(max_digits=10, decimal_places=2)
    metodo_pago         # CharField(choices=['efectivo', 'transferencia', 'tarjeta'])
```

### Modelo Administrador
```python
class Administrador(models.Model):
    usuario             # OneToOneField(User) → Relación 1:1
    telefono            # CharField(max_length=15)
```

---

## 🔄 Flujo de Funcionamiento

### Proceso de Solicitud de Préstamo

1. **Cliente se registra** en el sistema
2. **Cliente solicita préstamo** con monto y tasa de interés
3. **Administrador revisa** la solicitud
4. **Préstamo se aprueba** y se asigna fecha de vencimiento
5. **Cliente realiza pagos** según la programación
6. **Cada pago se registra** con fecha y método de pago
7. **Estado del préstamo** se actualiza automáticamente
8. **Préstamo se marca como pagado** cuando se completa

---

## 🛠️ Consultas Útiles (Django ORM)

```python
# Obtener todos los préstamos de un cliente
cliente = Cliente.objects.get(id=1)
prestamos = cliente.prestamos.all()

# Obtener todos los pagos de un préstamo
prestamo = Prestamo.objects.get(id=1)
pagos = prestamo.pagos.all()

# Obtener préstamos atrasados
prestamos_atrasados = Prestamo.objects.filter(estado='atrasado')

# Obtener total pagado en un préstamo
total_pagado = prestamo.pagos.aggregate(Sum('monto_pagado'))['monto_pagado__sum']
```

---

## 📋 API Endpoints (si aplica)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/clientes/` | Listar todos los clientes |
| POST | `/clientes/crear/` | Crear nuevo cliente |
| GET | `/prestamos/` | Listar todos los préstamos |
| POST | `/prestamos/crear/` | Crear nuevo préstamo |
| GET | `/pagos/` | Listar todos los pagos |
| POST | `/pagos/crear/` | Registrar nuevo pago |

---

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
python manage.py test

# Ejecutar pruebas de una aplicación específica
python manage.py test loans

# Ejecutar con cobertura de código
coverage run --source='.' manage.py test
coverage report
```

---

## 🔒 Seguridad

- ✅ Autenticación de usuarios integrada
- ✅ Protección CSRF en formularios
- ✅ Contraseñas hasheadas
- ✅ Control de acceso por roles
- ✅ Validación de entrada de datos

---

## 📝 Licencia

Este proyecto está disponible bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

## 👤 Autor

**Carolina**  
GitHub: [@carolina899](https://github.com/carolina899)  
Email: [Tu email aquí]

---

## 📞 Soporte y Contribuciones

Si encuentras problemas o tienes sugerencias:

1. Abre un [Issue](https://github.com/carolina899/Queen_Loans/issues)
2. Realiza un Fork y crea una Pull Request
3. Contacta directamente al autor

---

## 📅 Historial de Cambios

### Versión 1.0.0 (Actual)
- ✅ Implementación de modelos de Cliente, Préstamo, Pago y Administrador
- ✅ Relaciones de base de datos configuradas
- ✅ Interfaz web con HTML y CSS
- ✅ Documentación completa
- ✅ Corrección de errores y validaciones

---

**Última actualización:** Mayo 2026  
**Estado del Proyecto:** 🟢 Activo en desarrollo
