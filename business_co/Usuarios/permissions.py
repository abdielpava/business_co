#Gestión de permisos personalizados

from rest_framework.permissions import BasePermission

class AccesoPersonal(BasePermission):
    #Objetivo: brinda permiso de manipular objetos
    #solo si el usuario es el dueño del objeto o es un administrador

    def has_object_permission(self, request, view, obj):
        #request: contiene toda la informacion del usuario 
        #view: objeto tipo API
        #obj: es el objeto CRUD que se desea manipular

        #1: permiso absoluto
        if request.user.is_superuser: 
            return True
        
        #2: dueño del objeto
        if request.user.username == obj.username:
            return True
        return False 