from django.db import models
from django.forms import IntegerField


# Create your models here.
class Usuarios(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    cedula = models.IntegerField(default=0)
    correo = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField(default=0)
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
