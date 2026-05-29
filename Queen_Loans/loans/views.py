from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cliente, Prestamo, Pago
from .forms import RegistroClienteForm, PrestamoForm, PagoForm


def loan_list(request):
    prestamos = Prestamo.objects.all()
    return render(request, "loans/home.html", {"prestamos": prestamos})


def loan_create(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.tasa_interes = 5.0
            prestamo.save()
            form.save_m2m()
            messages.success(request, "Préstamo creado exitosamente")
            return redirect("Loans:loan_detail", loan_id=prestamo.id)
    else:
        form = PrestamoForm()
    return render(request, "loans/loan_form.html", {"form": form})


def loan_detail(request, loan_id):
    prestamo = get_object_or_404(Prestamo, id=loan_id)
    return render(request, "loans/loan_detail.html", {"prestamo": prestamo})


def loan_update(request, loan_id):
    prestamo = get_object_or_404(Prestamo, id=loan_id)
    if request.method == "POST":
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            prestamo = form.save()
            messages.success(request, "Préstamo actualizado")
            return redirect("Loans:loan_detail", loan_id=loan_id)
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, "loans/loan_form.html", {"form": form})


def loan_delete(request, loan_id):
    prestamo = get_object_or_404(Prestamo, id=loan_id)
    if request.method == "POST":
        prestamo.delete()
        messages.success(request, "Préstamo eliminado")
        return redirect("Loans:loan_list")
    return render(request, "loans/loan_confirm_delete.html", {"prestamo": prestamo})


def register_user(request):
    if request.method == "POST":
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email'].split('@')[0]
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(
                username=username,
                password=password,
                email=form.cleaned_data['email']
            )
            
            Cliente.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion']
            )
            
            messages.success(request, "Cliente registrado exitosamente")
            return redirect("Loans:login")
    else:
        form = RegistroClienteForm()
    return render(request, "loans/register.html", {"form": form})