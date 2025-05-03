
"""
Este archivo se encarga de ser intermediario entre el acceso a una URL y la serializacion JSON de la API RESTful.


Debido a la naturaleza del proyecto donde no se especifica un tratamiento para la API y sus registros
Se decidio usar la clase ModelViewSet
"""

from rest_framework.viewsets import ModelViewSet
from servicio_eventos.models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio
from .serializers import ClienteSerializer, EmpleadoSerializer, CoordinadorSerializer, ServicioSerializer, ReservaDeServicioSerializer



class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EmpleadoViewSet(ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class CoordinadorViewSet(ModelViewSet):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer    

class ServicioViewSet(ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class ReservaDeServicioViewSet(ModelViewSet):
    queryset = ReservaDeServicio.objects.all()
    serializer_class = ReservaDeServicioSerializer

