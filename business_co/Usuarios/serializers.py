from django.db.models import fields
from rest_framework import serializers

from Usuarios.models import *

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =  ['username', 'email', 'password']


class PerfilSerial(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

