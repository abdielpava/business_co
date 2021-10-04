from rest_framework import viewsets
from rest_framework import response
from Usuarios.serializers import * 
from Usuarios.permissions import *
from rest_framework import authentication, permissions


# Create your views here.
class UsuarioAPI(viewsets.ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (AccesoPersonal,)
    serializer_class = UserSerial
    queryset = get_user_model().objects.all() 


class PerfilAPI(viewsets.ModelViewSet):
    serializer_class = PerfilSerial
    queryset = Perfil.objects.all()


from rest_framework import views
from django.contrib.auth import logout, login 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class Login(views.APIView):
    def post(self, request):
        #reques nos envia toda la información del usuario
        if 'username' in request.data and 'password' in request.data:
            usuario = get_object_or_404(get_user_model(), username=request.data['username'])
            if usuario.check_password(request.data['password']):
                #la contraseña corresponde
                login(request, usuario)
                return Response("Se ha hecho login")
            return Response("Login o contraseña incorrecta")
        return Response("Información incompleta")

class Logout(views.APIView):
    def get(self, request):
        #cerrar la sesión
        nombreUsuario = request.user.username
        logout(request)
        return Response(nombreUsuario+" Has hecho logout")
     

