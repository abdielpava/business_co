
from rest_framework import viewsets
from Insumos.serializers import * 



# Create your views here.
class IngredienteAPI(viewsets.ModelViewSet):
    serializer_class = IngredienteSerial
    queryset  = Ingrediente.objects.all() 


class IngredientesEspAPI(viewsets.ModelViewSet):
    serializer_class = IngredientesEspSerial
    queryset = IngredientesEsp.objects.all()

class ProductoAPI(viewsets.ModelViewSet):
    serializer_class = ProductosSerial
    queryset = Producto.objects.all()
    
