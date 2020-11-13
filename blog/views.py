from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# -----------  para nuestos modelos --------------------
from .models import Cliente
from datetime import timezone
from .forms import ClienteForm


def login(request):
    return render(request, 'app/login.html', {})


def Inicio(request):
    return render(request, 'app/index.html')


def Acerca_de(request):
    return render(request, 'app/Acerca_de.html', {})


def Menu(request):
    return render(request, 'app/menu.html', {})


def Materiales(request):
    return render(request, 'app/material.html', {})


def Reciclaje(request):
    return render(request, 'app/reciclaje.html', {})



def Contacto(request):
    return render(request, 'app/contacto.html', {})



def Galeria(request):
    return render(request, 'app/galeria.html', {})


def listar_clientes(request):
    clientes = Cliente.objects.filter(nombre__contains='')
    return render(request, "app/listar_clientes.html", {'clientes': clientes})

def editar_cliente(request, cliente_id):
    instancia= Cliente.objects.get(id=cliente_id)
    form=  ClienteForm(instance=instancia)
    if request.method=="POST":
        form= ClienteForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
    return render(request, "app/editar_cliente.html",{'form':form})            

def borrar_cliente(request, cliente_id):    
    instacia= Cliente.objects.get(id=cliente_id)
    instacia.delete()
    return redirect('/listar_clientes')

class Cliente_Create(CreateView):
    model = Cliente
    form_class = ClienteForm
    templates_name = 'app/agregar_cliente.html'
    success_url = reverse_lazy('cliente_crear')

