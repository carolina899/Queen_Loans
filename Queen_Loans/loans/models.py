from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="prestamos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de interés anual")
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ("pendiente", "Pendiente"),
            ("pagado", "Pagado"),
            ("atrasado", "Atrasado"),
        ],
        default="pendiente"
    )

    def __str__(self):
        return f"Préstamo {self.id} - {self.cliente.nombre}"


class Pago(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateTimeField(default=timezone.now)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(
        max_length=20,
        choices=[
            ("efectivo", "Efectivo"),
            ("transferencia", "Transferencia"),
            ("tarjeta", "Tarjeta"),
        ],
        default="efectivo"
    )

    def __str__(self):
        return f"Pago {self.id} - Préstamo {self.prestamo.id}"

from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.usuario.username