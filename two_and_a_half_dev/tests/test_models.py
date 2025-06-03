import pytest
from servicio_eventos.models import Empleado, Coordinador, Servicio, Cliente, ReservaDeServicio
from datetime import timedelta
from django.utils import timezone


@pytest.fixture
def cliente():
    return Cliente.objects.create(
        nombre="Juan",
        apellido="Pérez",
        email="juan@example.com",
        telefono="123456789"
    )

@pytest.fixture
def empleado():
    return Empleado.objects.create(
        nombre="Juan",
        apellido="Perez",
        numero_legajo=123,
        activo=True
    )

@pytest.fixture
def coordinador():
    return Coordinador.objects.create(
        nombre="Ana",
        apellido="Gomez",
        numero_documento=456789,
        activo=True
    )

@pytest.fixture
def servicio():
    return Servicio.objects.create(
        nombre="Corte de cabello",
        descripcion="Servicio de corte de cabello básico",
        precio=500.00,
        activo=True
    )

@pytest.fixture
def cliente():
    return Cliente.objects.create(
        nombre="Carlos",
        apellido="Lopez",
        email="carlos@example.com",
        telefono="123456789"
    )

@pytest.fixture
def reserva_servicio(cliente, servicio, empleado, coordinador):
    fecha_servicio = timezone.now() + timedelta(days=3)
    return ReservaDeServicio.objects.create(
        fecha_servicio=fecha_servicio,
        cliente=cliente,
        servicio=servicio,
        empleado=empleado,
        coordinador=coordinador,
        total_precio=servicio.precio
    )


# Para ejecutar una etiqueta (previamente agregada al pytest.ini): pytest -m modelo
@pytest.mark.modelo
class Test_Cliente:

    @pytest.mark.django_db
    def test_cliente_delete(self,cliente):
        cliente.delete()
        with pytest.raises(Cliente.DoesNotExist):
            Cliente.objects.get(pk=cliente.pk)

""" Testeo de test_cliente_delete + explicación

¿Qué testea test_cliente_delete?
Que la instancia se crea correctamente en la base.

Que al llamar .delete() el objeto deja de existir en la base de datos.

Es un test funcional del comportamiento real del modelo y DB.

¿El scope o mock no deberían encargarse?
Scope (base de datos de test):
Solo aísla y limpia la BD para que cada test empiece limpio. No verifica nada sobre creación o eliminación, solo prepara entorno.

Mock:
Simula objetos/funciones sin usar DB real.
Aquí no tiene sentido porque queremos confirmar que .delete() realmente elimina en la BD.

Entonces:
Este test verifica la integridad de creación y borrado en la base real de test.

No es responsabilidad del scope ni del mock validar esto.

Para testear solo lógica de negocio sin DB sí usarías mocks o fakes. Pero aquí interesa el efecto real en la BD.

"""

@pytest.mark.modelo
@pytest.mark.django_db
def test_empleado_create_delete(empleado):
    assert empleado.nombre == "Juan"
    assert Empleado.objects.filter(pk=empleado.pk).exists()

    empleado.delete()
    with pytest.raises(Empleado.DoesNotExist):
        Empleado.objects.get(pk=empleado.pk)


@pytest.mark.modelo
@pytest.mark.django_db
def test_coordinador_create_delete(coordinador):
    assert coordinador.numero_documento == 456789
    assert Coordinador.objects.filter(pk=coordinador.pk).exists()

    coordinador.delete()
    with pytest.raises(Coordinador.DoesNotExist):
        Coordinador.objects.get(pk=coordinador.pk)


@pytest.mark.modelo
@pytest.mark.django_db
def test_servicio_precio_activo(servicio):
    assert servicio.precio == 500.00
    assert servicio.activo is True


@pytest.mark.modelo
@pytest.mark.django_db
def test_reserva_relaciones(reserva_servicio):
    assert reserva_servicio.servicio.nombre == "Corte de cabello"
    assert reserva_servicio.empleado.numero_legajo == 123
    assert reserva_servicio.coordinador.apellido == "Gomez"
    assert reserva_servicio.cliente.email == "carlos@example.com"


@pytest.mark.modelo
@pytest.mark.django_db
def test_reserva_creada_correctamente(reserva_servicio):
    assert reserva_servicio.total_precio == reserva_servicio.servicio.precio
    assert reserva_servicio.cliente.nombre == "Carlos"


    

@pytest.mark.modelo
@pytest.mark.django_db
def test_reserva_relaciones(reserva_servicio):
    assert reserva_servicio.cliente is not None
    assert reserva_servicio.servicio is not None
    assert reserva_servicio.empleado is not None
    assert reserva_servicio.coordinador is not None

@pytest.mark.modelo
@pytest.mark.django_db
def test_str_empleado(empleado):
    assert str(empleado) == "Juan Perez"

@pytest.mark.modelo
@pytest.mark.django_db
def test_str_coordinador(coordinador):
    assert str(coordinador) == "Ana Gomez"

@pytest.mark.modelo
@pytest.mark.django_db
def test_str_servicio(servicio):
    assert str(servicio) == "Corte de cabello"

@pytest.mark.modelo
@pytest.mark.django_db
def test_default_activo_empleado(empleado):
    assert empleado.activo is True

@pytest.mark.modelo
@pytest.mark.django_db
def test_default_activo_coordinador(coordinador):
    assert coordinador.activo is True

@pytest.mark.modelo
@pytest.mark.django_db
def test_default_activo_servicio(servicio):
    assert servicio.activo is True

@pytest.mark.modelo
@pytest.mark.django_db
def test_switch_activo(servicio):
    servicio.switch_activo()
    servicio.refresh_from_db()
    assert not servicio.activo
    servicio.switch_activo()
    servicio.refresh_from_db()
    assert servicio.activo

