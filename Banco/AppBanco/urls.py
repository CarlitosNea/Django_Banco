from django.urls import path
from AppBanco.views import *
from AppBanco.viewsLogin import *
from . import views
from django.conf import *
from django.conf.urls.static import *



""" urlpatterns = [
    path('clientes',ListadoClientes.as_view(),name='Clientes'),
    path('usuarios',ListadoUsuario.as_view(),name='Usuarios'),
    path('lineas',ListadoLineas.as_view(),name='Lineas_credito'),
    path('creditos',ListadoCreditos.as_view(),name='Creditos')
] """


urlpatterns = [
    path('cliente',ListadoClientes.as_view(),name="clientes"),
    path('insertar',InsertarCliente.as_view(),name="insertar"),
    path('actualizar/<pk>',ActualizarCliente.as_view(),name="actualizar"),
    path('eliminar/<pk>',Eliminar.as_view(),name="eliminar"),
    path('formularioInsertar',views.formularioInsertar,name='insertarf'),
    path('registro/',RegistrarUsuarioView.as_view(), name="registrar_usuario"),
    path('iniciarSesion/', IniciarSesionView.as_view(),name='iniciar_sesion'),
    path('updateCliente/', PerfilClienteView.as_view(), name="update_cliente")
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

