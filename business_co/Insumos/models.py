from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField() 
    unidades = models.CharField(max_length=200, default="g")
    cantidad = models.IntegerField()

    def __str__(self):
        #Identificar un objeto
        return self.nombre
    
    def costoUnitario(self):
        costoUnitario = 0
        pass


class IngredientesEsp(models.Model):
    #Ingredientes = models.ManyToManyField(Ingrediente)
    nombreIngEsp = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    precio = models.IntegerField()
    cantidadEsp = models.FloatField()
    descripcion = models.TextField()
    foto = models.ImageField(blank = True, null=True)
    #tiempoElaboracion = models.IntegerField()

    def __str__(self):
        return self.nombreIngEsp

    
    def costoIgredienteEsp(self):
        #valor de todos los ingredientes utilizados
        #mas el valor del tiempo que se emplea para hacerlo 
        ingredientes = MedidaIngrediente.objects.filter(ingredienteEsp=self)
        costo = 0
        for ingrediente in ingredientes:
            costo += ingrediente.ingrediente.cantidad / ingrediente.ingrediente.precio * ingrediente.cantidad
        return costo 


    def costoUnitario(self):
        #el valor del producto ya preparado 
        pass

class MedidaIngrediente(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    ingredienteEsp = models.ForeignKey(IngredientesEsp, on_delete=CASCADE)
    cantidad = models.FloatField()
    
    def __str__(self):
         return self.ingredienteEsp.nombreIngEsp



class Producto(models.Model):
    ingredientes = models.ManyToManyField(Ingrediente)
    ingredientesEsp = models.ManyToManyField(IngredientesEsp)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    contenido = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.nombre


