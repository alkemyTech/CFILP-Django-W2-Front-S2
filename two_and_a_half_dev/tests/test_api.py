import pytest
from api.serializers import ClienteSerializer, EmpleadoSerializer, CoordinadorSerializer, ServicioSerializer, \
      ReservaDeServicioSerializer
from servicio_eventos.models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio
import requests
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def cliente():
    return Cliente.objects.create(
        id=1,
        nombre="Juan",
        apellido="Pérez",
        activo=True
    )

@pytest.fixture
def empleado():
    return Empleado.objects.create(
        id=1,
        nombre="Ana",
        apellido="Gómez",
        numero_legajo=12345,
        activo=True
    )

@pytest.fixture
def coordinador():
    return Coordinador.objects.create(
        id=1,
        nombre="Luis",
        apellido="Martínez",
        numero_documento=12345678,
        #fecha_alta= models.DateTimeField(auto_now_add=True),
        activo=True
    )

@pytest.fixture
def servicio():
    return Servicio.objects.create(
        id=1,
        nombre="Catering",
        descripcion="Servicio de catering para eventos",
        precio=1500.00,
        activo=True
    )

# @pytest.fixture
# def reserva_de_servicio(cliente, servicio, empleado, coordinador):
#     cliente = Cliente.objects.create(nombre="Juan")
#     servicio = Servicio.objects.create(nombre="Catering")
#     empleado = Empleado.objects.create(nombre="Pepito Grillo")
#     coordinador = Coordinador.objects.create(nombre="Pinocho")

#     return ReservaDeServicio.objects.create(
#         fecha_reserva=timezone.now(),
#         fecha_servicio=timezone.now(),
#         cliente=cliente,
#         servicio=servicio,
#         empleado=empleado,
#         coordinador=coordinador,
#         total_precio=1500.00
#     )


#/////////////////////////////// CLIENTE ///////////////////////////////////////
#Verifica que un objeto Django se convierte correctamente en datos JSON.
@pytest.mark.django_db
def test_serializer_cliente(cliente):
    serializer = ClienteSerializer(instance=cliente)
    expected_data = {
        "id": cliente.id,
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "activo": cliente.activo
    }
    assert serializer.data == expected_data

#Comprueba que los datos JSON se validan y se transforman en una instancia de Cliente.
@pytest.mark.django_db
def test_deserializer_cliente(cliente):
    data = {
        "id": cliente.id,
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "activo": cliente.activo
    }
    serializer = ClienteSerializer(data=data)

    assert serializer.is_valid()
    assert serializer.validated_data["nombre"] == "Juan"
    assert serializer.validated_data["apellido"] == "Pérez"
    assert serializer.validated_data["activo"] is True

#Verifica que el serializador detecta datos incorrectos
@pytest.mark.django_db
def test_validacion_cliente():
    data = {"nombre": "", "apellido": "", "activo": "no válido"} 
    serializer = ClienteSerializer(data=data)

    assert not serializer.is_valid() 
    assert "nombre" in serializer.errors
    assert "apellido" in serializer.errors
    assert "activo" in serializer.errors

#Verifica que el serializador transforma datos del modelo en estructuras de Python.
@pytest.mark.django_db
def test_cliente_conversion_automatica(cliente):
    serializer = ClienteSerializer(instance=cliente)
    assert isinstance(serializer.data, dict)
    assert isinstance(serializer.data["activo"], bool)

#/////////////////////////////// EMPLEADO ///////////////////////////////////////
@pytest.mark.django_db
def test_serializer_empleado(empleado):
    serializer =  EmpleadoSerializer(instance=empleado)
    serialized_data = serializer.data
    expected_data = {
        "id": empleado.id,
        "nombre": empleado.nombre,
        "apellido": empleado.apellido,
        "numero_legajo": empleado.numero_legajo,
        "activo": empleado.activo
    }
    assert serialized_data == expected_data

@pytest.mark.django_db
def test_deserializer_empleado(empleado):
    data = {
        "id": empleado.id,
        "nombre": empleado.nombre,
        "apellido": empleado.apellido,
        "numero_legajo": empleado.numero_legajo,
        "activo": empleado.activo
    }
    serializer = EmpleadoSerializer(data=data)

    assert serializer.is_valid()
    assert serializer.validated_data["nombre"] == "Ana"
    assert serializer.validated_data["apellido"] == "Gómez"
    assert serializer.validated_data["numero_legajo"] == 12345
    assert serializer.validated_data["activo"] is True

@pytest.mark.django_db
def test_validacion_empleado():
    data = {"nombre": "", "apellido": "", "numero_legajo":"", "activo": "no válido"} 
    serializer = EmpleadoSerializer(data=data)

    assert not serializer.is_valid() 
    assert "nombre" in serializer.errors
    assert "apellido" in serializer.errors
    assert "numero_legajo" in serializer.errors
    assert "activo" in serializer.errors

@pytest.mark.django_db
def test_empleado_conversion_automatica(empleado):
    serializer = EmpleadoSerializer(instance=empleado)
    assert isinstance(serializer.data, dict)
    assert isinstance(serializer.data["activo"], bool)

#/////////////////////////////// COORDINADOR ///////////////////////////////////////
@pytest.mark.django_db
def test_serializer_coordinador(coordinador):
    serializer =  CoordinadorSerializer(instance=coordinador)
    serialized_data = serializer.data
    expected_data = {
        "id": coordinador.id,
        "nombre": coordinador.nombre,
        "apellido": coordinador.apellido,
        "numero_documento": coordinador.numero_documento,
        #"fecha_alta": coordinador.fecha_alta,
        "activo": coordinador.activo
    }
    serialized_data.pop("fecha_alta", None)  # Elimina "fecha_alta"
    assert serialized_data == expected_data

@pytest.mark.django_db
def test_deserializer_coordinador(coordinador):
    data = {
        "id": coordinador.id,
        "nombre": coordinador.nombre,
        "apellido": coordinador.apellido,
        "numero_documento": coordinador.numero_documento,
        #"fecha_alta": coordinador.fecha_alta,
        "activo": coordinador.activo
    }
    serializer = CoordinadorSerializer(data=data)

    assert serializer.is_valid()
    assert serializer.validated_data["nombre"] == "Luis"
    assert serializer.validated_data["apellido"] == "Martínez"
    assert serializer.validated_data["numero_documento"] == 12345678
    #assert serializer.validated_data["fecha_alta"] == coordinador.fecha_alta
    assert serializer.validated_data["activo"] is True

@pytest.mark.django_db
def test_validacion_coordinador():
    data = {"nombre": "", "apellido": "", "numero_documento":"", "activo": "no válido"} 
    serializer = CoordinadorSerializer(data=data)

    assert not serializer.is_valid() 
    assert "nombre" in serializer.errors
    assert "apellido" in serializer.errors
    assert "numero_documento" in serializer.errors
    #assert "fecha_alta" in serializer.errors
    assert "activo" in serializer.errors

@pytest.mark.django_db
def test_coordinador_conversion_automatica(coordinador):
    serializer = CoordinadorSerializer(instance=coordinador)
    assert isinstance(serializer.data, dict)
    assert isinstance(serializer.data["activo"], bool)

#/////////////////////////////// SERVICIO ///////////////////////////////////////
@pytest.mark.django_db
def test_serializer_servicio(servicio):
    serializer =  ServicioSerializer(instance=servicio)
    serialized_data = serializer.data
    expected_data = {
        "id": servicio.id,
        "nombre": servicio.nombre,
        "descripcion": servicio.descripcion,
        "precio": servicio.precio,
        "activo": servicio.activo
    }
    serialized_data["precio"] = float(serialized_data["precio"])  # Convertir a número float
    assert serialized_data == expected_data

@pytest.mark.django_db
def test_deserializer_servicio(servicio):
    data = {
        "id": servicio.id,
        "nombre": servicio.nombre,
        "descripcion": servicio.descripcion,
        "precio": servicio.precio,
        "activo": servicio.activo
    }
    serializer = ServicioSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["nombre"] == "Catering"
    assert serializer.validated_data["descripcion"] == "Servicio de catering para eventos"
    assert serializer.validated_data["precio"] == 1500.00
    assert serializer.validated_data["activo"] is True

@pytest.mark.django_db
def test_validacion_servicio():
    data = {"nombre": "", "descripcion": "", "precio":"", "activo": "no válido"} 
    serializer = ServicioSerializer(data=data)

    assert not serializer.is_valid() 
    assert "nombre" in serializer.errors
    assert "descripcion" in serializer.errors
    assert "precio" in serializer.errors
    assert "activo" in serializer.errors

@pytest.mark.django_db
def test_servicio_conversion_automatica(servicio):
    serializer = ServicioSerializer(instance=servicio)
    assert isinstance(serializer.data, dict)
    assert isinstance(serializer.data["activo"], bool)

# #/////////////////////////////// RESERVA DE SERVICIO ///////////////////////////////////////
# @pytest.mark.django_db
# def test_serializer_reserva_de_servicio(reserva_de_servicio):
#     serializer =  ReservaDeServicioSerializer(instance=reserva_de_servicio)
#     serialized_data = serializer.data
#     expected_data = {
#         "id": reserva_de_servicio.id,
#         #"fecha_reserva": reserva_de_servicio.fecha_reserva,
#         #"fecha_servicio": reserva_de_servicio.fecha_servicio,
#         "cliente": reserva_de_servicio.cliente,
#         "servicio": reserva_de_servicio.servicio,
#         "empleado": reserva_de_servicio.empleado,
#         "coordinador": reserva_de_servicio.coordinador,
#         "total_precio": reserva_de_servicio.total_precio
#     }
#     serialized_data.pop("fecha_reserva", None)  # Elimina "fecha_reserva"
#     serialized_data.pop("fecha_servicio", None)  # Elimina "fecha_servicio"
#     assert serialized_data == expected_data

# @pytest.mark.django_db
# def test_deserializer_reserva_de_servicio(reserva_de_servicio):
#     data = {
#         "id": reserva_de_servicio.id,
#         #"fecha_reserva": reserva_de_servicio.fecha_reserva,
#         #"fecha_servicio": reserva_de_servicio.fecha_servicio,
#         "cliente": reserva_de_servicio.cliente,
#         "servicio": reserva_de_servicio.servicio,
#         "empleado": reserva_de_servicio.empleado,
#         "coordinador": reserva_de_servicio.coordinador,
#         "total_precio": reserva_de_servicio.total_precio
#     }
#     serializer = ReservaDeServicioSerializer(data=data)
#     assert serializer.is_valid()
#     assert serializer.validated_data["cliente"] == "Juan"
#     assert serializer.validated_data["servicio"] == "Catering"
#     assert serializer.validated_data["empleado"] == "Pepito Grillo"
#     assert serializer.validated_data["coordinador"] == "Pinocho"
#     assert serializer.validated_data["total_precio"] == 1500.00
#     #assert serializer.validated_data["fecha_reserva"] == reserva_de_servicio.fecha_reserva
#     #assert serializer.validated_data["fecha_servicio"] == reserva_de_servicio.fecha_servicio

# @pytest.mark.django_db
# def test_validacion_reserva_de_servicio():
#     data = {"fecha_reserva": "", "fecha_servicio": "", "cliente":"", "servicio": "", "empleado": "", "coordinador": "", "total_precio": ""} 
#     serializer = ReservaDeServicioSerializer(data=data)

#     assert not serializer.is_valid() 
#     #assert "fecha_reserva" in serializer.errors
#     #assert "fecha_servicio" in serializer.errors
#     assert "cliente" in serializer.errors
#     assert "servicio" in serializer.errors
#     assert "empleado" in serializer.errors
#     assert "coordinador" in serializer.errors
#     assert "total_precio" in serializer.errors

# @pytest.mark.django_db
# def test_reserva_de_servicio_conversion_automatica(reserva_de_servicio):
#     serializer = ReservaDeServicioSerializer(instance=reserva_de_servicio)
#     assert isinstance(serializer.data, dict)
#     assert isinstance(serializer.data["total_precio"], float)

#/////////////////////////////// URL ///////////////////////////////////////
@pytest.mark.django_db
@pytest.mark.parametrize("endpoint", [
    "cliente",
    "empleado",
    "coordinador",
    "servicios",
    "reservadeservicio"
])
def test_router_endpoints(live_server, endpoint):
    url = f"{live_server.url}/api/{endpoint}/"
    response = requests.get(url)
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa

""""PRUEBA DE CREACIÓN"""
@pytest.mark.django_db
def test_creacion_cliente():
    client = APIClient()
    url = reverse("cliente-list")  # Endpoint de creación
    data = {"nombre": "Juan", "apellido": "Pérez", "activo": True}
    response = client.post(url, data, format="json")
    assert response.status_code == 201  # Verifica que se creó correctamente
    assert response.json()["nombre"] == "Juan"

@pytest.mark.django_db
def test_creacion_empleado():
    client = APIClient()
    url = reverse("empleado-list")
    data = {"nombre": "Ana", "apellido": "Gómez", "numero_legajo": 12345, "activo": True}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.json()["nombre"] == "Ana"

@pytest.mark.django_db
def test_creacion_coordinador():
    client = APIClient()
    url = reverse("coordinador-list")
    data = {"nombre": "Luis", "apellido": "Martínez", "numero_documento": 12345678, "activo": True}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.json()["nombre"] == "Luis"

@pytest.mark.django_db
def test_creacion_servicio():
    client = APIClient()
    url = reverse("servicio-list")
    data = {"nombre": "Catering", "descripcion": "Servicio de catering para eventos", "precio": 1500.00, "activo": True}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.json()["nombre"] == "Catering"

""""" VALIDACIÓN REPUESTAS JSON """
@pytest.mark.django_db
def test_respuesta_cliente():
    client = APIClient()
    url = reverse("cliente-list")
    response = client.get(url)
    assert isinstance(response.json(), list)

@pytest.mark.django_db
def test_lista_empleados():
    client = APIClient()
    url = reverse("empleado-list")
    response = client.get(url)
    assert isinstance(response.json(), list)  # Confirmamos que devuelve una lista

@pytest.mark.django_db
def test_lista_coordinadores():
    client = APIClient()
    url = reverse("coordinador-list")
    response = client.get(url)
    assert isinstance(response.json(), list)

@pytest.mark.django_db
def test_lista_servicios():
    client = APIClient()
    url = reverse("servicio-list")
    response = client.get(url)
    assert isinstance(response.json(), list)

