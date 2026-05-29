from django import forms
from .models import Cliente, Prestamo, Pago


class RegistroClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'email', 'telefono', 'direccion')
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('cliente', 'monto', 'fecha_vencimiento', 'estado', 'categorias')


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ('prestamo', 'monto_pagado', 'metodo_pago')
