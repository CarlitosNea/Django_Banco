from django.contrib import admin
from AppBanco.models import *

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('documento','nombre_usu','clave')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('documento','nombre','apellido','correo','telefono','direccion','genero')


@admin.register(Lineas_de_credito)
class LineasAdmin(admin.ModelAdmin):
    list_display=('codigo','nombre_credito','monto_maximo','plazo_maximo')


@admin.register(Creditos)
class CreditosAdmin(admin.ModelAdmin):
    list_display=('documento_cliente','cod_lineacredito','monto_prestado','plazo',)

