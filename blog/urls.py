from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index',views.Inicio),
    path('agregar_cliente', views.Cliente_Create.as_view(), name="cliente_crear"),
    path('listar_clientes',views.listar_clientes),
    path('editar_cliente/<int:cliente_id>', views.editar_cliente),
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente),
    path('menu', views.Menu),

    path('login', views.login),
    path('material', views.Materiales),
    path('reciclaje', views.Reciclaje),
    path('galeria', views.Galeria),
    path('Acerca_de', views.Acerca_de),
    path('contacto', views.Contacto),
   
]
