from django.db import models

# Create your models here.

class registro(models.Model):
    correo = models.EmailField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=50)

class metas(models.Model):
    nombremeta = models.CharField(max_length=50, primary_key=True)
    descripcion = models.CharField(max_length=250)
    recompensa = models.CharField(max_length=50)
    fechameta = models.DateTimeField()
    