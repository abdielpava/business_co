#direcciones locales
from Insumos.views import IngredienteAPI, IngredientesEspAPI, ProductoAPI
from django.urls import path, include 
from rest_framework.routers import DefaultRouter
#from Usuarios.views import * 


router = DefaultRouter()
router.register('ingrediente', IngredienteAPI,  basename="ingrediente")
router.register('ingredienteEsp', IngredientesEspAPI, basename="ingredienteEsp")
router.register('productos', ProductoAPI, basename="productos")

urlpatterns = [
    path('crud/', include(router.urls))
]

