
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('insumos/api/', include('Insumos.urls')),
    path('users/api/', include('Usuarios.urls'))
]
