from django.urls import path
from .views import *


urlpatterns = [
    path('clientes',ListadoClientes.as_view(),name='Clientes'),
    path('usuarios',ListadoUsuario.as_view(),name='Usuarios'),
    path('lineas',ListadoLineas.as_view(),name='Lineas_credito'),
    path('creditos',ListadoCreditos.as_view(),name='Creditos')
]

