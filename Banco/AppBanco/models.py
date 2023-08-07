# Create your models here.
from django.conf import settings
from django.contrib.auth.models import *
from django.db import models
from .enum import plazo

# Create your models here.


class Usuario(models.Model):
    documento=models.TextField(max_length=10)
    nombre_usu=models.TextField(max_length=50)
    clave=models.TextField(max_length=20)


class Cliente(models.Model):
    #documento = models.OneToOneField(User, on_delete=models.CASCADE,max_length=10, primary_key=True)
    documento = models.TextField(max_length=10, null=False, primary_key=True)
    nombre=models.TextField(max_length=20)
    apellido=models.TextField(max_length=20)
    correo=models.EmailField(max_length=254)
    telefono=models.TextField(max_length=20)
    direccion=models.TextField(max_length=20)
    genero=models.TextField(max_length=10)

class User(AbstractUser):
    rol = models.CharField(max_length=100)
    imagen = models.ImageField(default="", upload_to='img/', null=True, blank=True)
    documento = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)

class Lineas_de_credito(models.Model):
    codigo=models.PositiveSmallIntegerField(verbose_name="Codigo",primary_key=True)
    nombre_credito=models.TextField(max_length=20)
    monto_maximo = models.PositiveBigIntegerField(verbose_name="Monto maximo")
    plazo_maximo=models.PositiveSmallIntegerField(verbose_name="Plazo maximo")


class Creditos(models.Model):
    documento_cliente=models.ForeignKey(Cliente, null=False,on_delete=models.CASCADE)
    cod_lineacredito=models.ForeignKey(Lineas_de_credito,null=False,on_delete=models.CASCADE)
    monto_prestado = models.PositiveBigIntegerField(verbose_name="Prestado")
    plazo=models.PositiveSmallIntegerField(verbose_name="Plazo maximo",choices=plazo,default=6)
