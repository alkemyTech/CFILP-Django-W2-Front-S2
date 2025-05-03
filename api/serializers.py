from rest_framework import serializers

from servicio_eventos.models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nombre", "apellido", "activo"]


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ["id", "nombre", "apellido", "numero_legajo", "activo"]

class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = ["id", "nombre", "apellido", "numero_documento", "fecha_alta", "activo"]   

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ["id", "nombre", "descripcion", "precio", "activo"]    

class ReservaDeServicioSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    empleado = EmpleadoSerializer(read_only=True)
    coordinador = CoordinadorSerializer(read_only=True)
    servicio = ServicioSerializer(read_only=True)

    class Meta:
        model = ReservaDeServicio
        fields = ["id", "fecha_reserva", "fecha_servicio", "cliente", "servicio", "empleado", "coordinador", "total_precio"]


        

