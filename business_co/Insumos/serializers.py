from django.db.models import fields
from rest_framework import serializers
from Insumos.models import * 

class IngredienteSerial(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente 
        fields = '__all__'


class IngredientesEspSerial(serializers.ModelSerializer):
    class Meta:
        model = IngredientesEsp 
        fields = '__all__'

class ProductosSerial(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'