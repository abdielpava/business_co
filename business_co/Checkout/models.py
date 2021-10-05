from django.db import models
from django.db.models.fields import BooleanField
from Insumos.models  import Producto
from Usuarios.models import Perfil 


# Create your models here.
class CarritoCompras(models.Model):
    usuario =  models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    dcto = models.FloatField(default=0)
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False) 
    #(null=True, blank=True)


    def __str__(self):
        return str(self.usuario) + " - "+ str(self.fecha)

    @property
    def total(self):
        total = 0
        for articulo in self.articulo_set.all():
            total += articulo.subtotal()
        return total 
    
    def numArt(self):
        cantArt = 0
        for articulo in self.articulo_set.all():
            cantArt += articulo.cantidad 
        return cantArt   

    
class Articulo(models.Model):
      carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
      producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
      cantidad = models.IntegerField()

      # def tipoEl(self):
      #    from Productos.serializers import TipoSerial
      
      def __str__(self):
        #return self.carrito+" - "+self.producto.nombre  
        return self.carrito.__str__() + " / " + self.producto.nombre
     
      def subtotal(self):
          return self.producto.precio*self.cantidad
    

class infoEnvio(models.Model):
     carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
     nombre = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     direccion = models.CharField(max_length=300)
     paais = models.CharField(max_length=300)
     departamento = models.CharField(max_length=300)
     ciudad = models.CharField(max_length=300)

     def __str__(self):
        return self.nombre 