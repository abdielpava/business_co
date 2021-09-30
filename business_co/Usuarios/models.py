from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Perfil(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    #edad = nombres = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.usuario.email 
