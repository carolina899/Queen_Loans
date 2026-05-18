from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from django_http import HttpResponse
# Create your views here.

User = get_user_model()

def registrar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fecha_nacimiento_str = request.POST.get('fecha_nacimiento')

        if fecha_nacimiento_str:
            fecha_nacimiento = datetime.strftime(fecha_nacimiento_str, '%Y-%m-%d').date()
            hoy = timezone.now().datetime() 
            edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day < (fecha_nacimiento.month, fecha_nacimiento.day)))
            if edad < 18:
            
               return HttpResponse("Error debes ser mayor de 18 años para registrarte ", status=400)
            User.objects.create_superuser(
                username=usuario,
                email=email,
                password=password,
                fecha_nacimiento=fecha_nacimiento_str
            )
            return HttpResponse("Usuario creado con exito. redirigiendo a login  ...")