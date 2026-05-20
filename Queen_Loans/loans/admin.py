from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cliente, Prestamo, Pago, Administrador

admin.site.register(Cliente)
admin.site.register(Prestamo)
admin.site.register(Pago)
admin.site.register(Administrador)
