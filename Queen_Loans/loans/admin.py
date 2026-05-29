from django.contrib import admin
from .models import Cliente, Categoria, Prestamo, Pago, Administrador


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


class PagoInline(admin.TabularInline):
    model = Pago
    extra = 1


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'monto', 'estado', 'fecha_vencimiento')
    list_filter = ('estado', 'fecha_inicio')
    search_fields = ('cliente__nombre', 'cliente__apellido')
    filter_horizontal = ('categorias',)
    inlines = [PagoInline]


class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'prestamo', 'fecha_pago', 'monto_pagado', 'metodo_pago')
    list_filter = ('metodo_pago', 'fecha_pago')
    search_fields = ('prestamo__id',)


class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono')
    search_fields = ('usuario__username',)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Administrador, AdministradorAdmin)
