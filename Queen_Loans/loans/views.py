from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime

from .models import Cliente 

User = get_user_model()

def registrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        password = request.POST.get('password')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        fecha_nacimiento_str = request.POST.get('fecha_nacimiento')

        if fecha_nacimiento_str:
            try:
               
                fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
            except ValueError:
                return HttpResponse("Formato de fecha inválido.", status=400)
            
            
            hoy = timezone.now().date()
            edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            
            if edad < 18:
                return HttpResponse("Error: debes ser mayor de 18 años para registrarte.", status=400)
            
            
            nuevo_usuario = User.objects.create_user(
                username=usuario,
                email=email,
                password=password
            )
            
            
            Cliente.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                direccion=direccion
            )
            
            return HttpResponse("Usuario y Cliente creados con éxito. Redirigiendo...")
            
    return render(request, 'tu_plantilla_de_registro.html')