from django.urls import path, include
from django.urls import path, include 
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from Usuarios.views import * 


router = DefaultRouter()
router.register('usuarios', UsuarioAPI)
router.register('perfiles', PerfilAPI)

urlpatterns = [
    path('crud/', include(router.urls)),
    path('logout', Logout.as_view()),
    path('login', Login.as_view())
]

