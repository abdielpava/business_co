from django.db import models


# Create your models here.
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField() 
    unidades = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        #Identificar un objeto
        return self.nombre
    
    def costoUnitario(self):
        pass


class IngredientesEsp(models.Model):
    nombreIngrediente = models.ManyToManyField(Ingrediente)
    nombreIngEsp = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(blank = True, null=True)

    def __str__(self):
        return self.nombreIngEsp

    
    def costoIgredienteEsp(self):
        pass

    def costoUnitario(self):
        pass

class Producto(models.Model):
    ingredientes = models.ManyToManyField(Ingrediente)
    ingredientesEsp = models.ManyToManyField(IngredientesEsp)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    contenido = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.nombre


