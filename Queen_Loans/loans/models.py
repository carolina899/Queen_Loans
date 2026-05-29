from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Cliente(models.Model):
    """Modelo que representa un cliente del sistema"""
    nombre = models.CharField(max_length=100, help_text="Nombre del cliente")
    apellido = models.CharField(max_length=100, help_text="Apellido del cliente")
    email = models.EmailField(unique=True, help_text="Email único del cliente")
    telefono = models.CharField(max_length=15, blank=True, null=True, help_text="Teléfono de contacto")
    direccion = models.TextField(blank=True, null=True, help_text="Dirección del cliente")
    fecha_registro = models.DateTimeField(default=timezone.now, help_text="Fecha de registro en el sistema")
    fecha_nacimiento = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del cliente")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Categoria(models.Model):
    """Modelo que representa las categorías de préstamos"""
    nombre = models.CharField(max_length=100, unique=True, help_text="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción detallada de la categoría")
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación de la categoría")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    """Modelo que representa un préstamo"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="prestamos", help_text="Cliente que solicita el préstamo")
    categorias = models.ManyToManyField(Categoria, related_name="prestamos", help_text="Categorías a las que pertenece el préstamo")
    monto = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monto del préstamo")
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de interés anual")
    fecha_inicio = models.DateField(default=timezone.now, help_text="Fecha de inicio del préstamo")
    fecha_vencimiento = models.DateField(help_text="Fecha de vencimiento del préstamo")
    estado = models.CharField(
        max_length=20,
        choices=[
            ("pendiente", "Pendiente"),
            ("pagado", "Pagado"),
            ("atrasado", "Atrasado"),
        ],
        default="pendiente",
        help_text="Estado actual del préstamo"
    )

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"Préstamo {self.id} - {self.cliente.nombre} - ${self.monto}"


class Pago(models.Model):
    """Modelo que representa los pagos de préstamos"""
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="pagos", help_text="Préstamo al que corresponde el pago")
    fecha_pago = models.DateTimeField(default=timezone.now, help_text="Fecha en que se realizó el pago")
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monto que se pagó")
    metodo_pago = models.CharField(
        max_length=20,
        choices=[
            ("efectivo", "Efectivo"),
            ("transferencia", "Transferencia"),
            ("tarjeta", "Tarjeta"),
        ],
        default="efectivo",
        help_text="Método de pago utilizado"
    )

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ['-fecha_pago']

    def __str__(self):
        return f"Pago {self.id} - Préstamo {self.prestamo.id} - ${self.monto_pagado}"


class Administrador(models.Model):
    """Modelo que representa un administrador del sistema"""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Usuario de Django asociado")
    telefono = models.CharField(max_length=15, blank=True, null=True, help_text="Teléfono del administrador")
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación del administrador")

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
        return f"Admin - {self.usuario.username}"
