from django.contrib import admin
from .models import Cliente, Categoria, Prestamo, Pago, Administrador


class ClienteAdmin(admin.ModelAdmin):
    """Administrador personalizado para el modelo Cliente"""
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_registro')
    list_filter = ('fecha_registro', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'email')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'fecha_nacimiento')
        }),
        ('Información de Contacto', {
            'fields': ('email', 'telefono', 'direccion')
        }),
        ('Información del Sistema', {
            'fields': ('fecha_registro',),
            'classes': ('collapse',)
        }),
    )


class CategoriaAdmin(admin.ModelAdmin):
    """Administrador personalizado para el modelo Categoría"""
    list_display = ('nombre', 'fecha_creacion', 'cantidad_prestamos')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_creacion',)
    
    def cantidad_prestamos(self, obj):
        return obj.prestamos.count()
    cantidad_prestamos.short_description = 'Cantidad de Préstamos'


class PagoInline(admin.TabularInline):
    """Inline para mostrar pagos dentro del admin de préstamo"""
    model = Pago
    extra = 1
    fields = ('fecha_pago', 'monto_pagado', 'metodo_pago')
    readonly_fields = ('fecha_pago',)


class PrestamoAdmin(admin.ModelAdmin):
    """Administrador personalizado para el modelo Préstamo"""
    list_display = ('id', 'cliente', 'monto', 'tasa_interes', 'estado', 'fecha_vencimiento', 'mostrar_categorias')
    list_filter = ('estado', 'fecha_inicio', 'fecha_vencimiento', 'categorias')
    search_fields = ('cliente__nombre', 'cliente__apellido')
    inlines = [PagoInline]
    readonly_fields = ('fecha_inicio',)
    filter_horizontal = ('categorias',)  # Para manejar mejor la relación M2M
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('cliente',)
        }),
        ('Detalles del Préstamo', {
            'fields': ('monto', 'tasa_interes', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_vencimiento')
        }),
        ('Categorías', {
            'fields': ('categorias',)
        }),
    )
    
    def mostrar_categorias(self, obj):
        return ", ".join([cat.nombre for cat in obj.categorias.all()])
    mostrar_categorias.short_description = 'Categorías'


class PagoAdmin(admin.ModelAdmin):
    """Administrador personalizado para el modelo Pago"""
    list_display = ('id', 'prestamo', 'fecha_pago', 'monto_pagado', 'metodo_pago', 'cliente_pago')
    list_filter = ('metodo_pago', 'fecha_pago')
    search_fields = ('prestamo__id', 'prestamo__cliente__nombre')
    readonly_fields = ('fecha_pago',)
    fieldsets = (
        ('Información del Préstamo', {
            'fields': ('prestamo',)
        }),
        ('Detalles del Pago', {
            'fields': ('monto_pagado', 'metodo_pago')
        }),
        ('Fecha', {
            'fields': ('fecha_pago',)
        }),
    )
    
    def cliente_pago(self, obj):
        return obj.prestamo.cliente.nombre
    cliente_pago.short_description = 'Cliente'


class AdministradorAdmin(admin.ModelAdmin):
    """Administrador personalizado para el modelo Administrador"""
    list_display = ('usuario', 'telefono', 'fecha_creacion')
    search_fields = ('usuario__username', 'usuario__email')
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Información del Usuario', {
            'fields': ('usuario',)
        }),
        ('Información de Contacto', {
            'fields': ('telefono',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )


# Registrar los modelos con sus administradores personalizados
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Administrador, AdministradorAdmin)
