from rest_framework import serializers
from Insumos.models import * 

class IingredienteSerial(serializers.ModelSerializer):
    class meta:
        model = Ingrediente 
        fields = '__all__'


class IngredientesEspSerial(serializers.ModelSerializer):
    class meta:
        model = IngredientesEsp 
        fields = '__all__'

class ProductosSerial(serializers.ModelSerializer):
    class meta:
        model = Producto
        fields = '__all__'