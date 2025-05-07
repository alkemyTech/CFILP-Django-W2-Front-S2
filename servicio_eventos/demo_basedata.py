"""
El proposito de esta clase es crear una base de datos de ejemplo para ver funcionalidades de la pagina web
de eventos.

Para utilizar debe ejecutarse el siguiente comando en la terminal estando a la altura de manage.py:
(Previamente debe haber hecho las migraciones para que la base de datos exista (no necesariamente con datos))

# => python manage.py shell
# => from servicio_eventos.demo_basedata import create_bd_example
# => create_bd_example()
"""

"""
Metodo para crear un superusuario para acceder a la pagina con permisos de administrador. 
    (Incluido Home)
"""
    
from django.contrib.auth.models import User

def crear_superusuario():
    # Crear el superusuario
    username = 'admin1'
    email = 'na'
    password = 'admin123'  # Cambia por un password seguro
    
    # Si el superusuario no existe, lo creamos
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuario '{username}' creado exitosamente.")
    else:
        print(f"El superusuario '{username}' ya existe.")


from .models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio

def create_bd_example():
    crear_superusuario()

    # Generamos una lista de Diccionarios para que la creacion sea mas simple:
    # Recorremos el arreglo de diccionarios y creamos los objetos en la base de datos

    clientes = [{"nombre": "Juan", "apellido": "Pérez", "activo": True},
                {"nombre": "Ana", "apellido": "Gómez", "activo": True},
               {"nombre": "Luis", "apellido": "Martínez", "activo": False},
               {"nombre": "María", "apellido": "López", "activo": True}]
    
    empleados = [{"nombre": "Carlos", "apellido": "Fernández", "numero_legajo": 123, "activo": True},
                {"nombre": "Laura", "apellido": "Ramírez", "numero_legajo": 456, "activo": True},
                {"nombre": "Pedro", "apellido": "Sánchez", "numero_legajo": 789, "activo": False},
                {"nombre": "Lucía", "apellido": "Torres", "numero_legajo": 101, "activo": True}]
    
    coordinadores = [{"nombre": "Javier", "apellido": "García", "numero_documento": 12345678, "activo": False},
                    {"nombre": "Sofía", "apellido": "Hernández", "numero_documento": 87654321, "activo": True},
                    {"nombre": "Diego", "apellido": "Cruz", "numero_documento": 11223344, "activo": True},
                    {"nombre": "Valentina", "apellido": "Mendoza", "numero_documento": 44332211, "activo": True}]
    
    servicios = [{"nombre": "Catering", "descripcion": "Servicio de catering para eventos", "precio": 1000, "activo": True},
                {"nombre": "Decoración", "descripcion": "Servicio de decoración para eventos", "precio": 500, "activo": True},
                {"nombre": "Fotografía", "descripcion": "Servicio de fotografía para eventos", "precio": 800, "activo": True},
                {"nombre": "Música", "descripcion": "Servicio de música para eventos", "precio": 1200, "activo": False}]
    
    # Creamos los objetos en la base de datos
    # For recorre 'clientes' donde cada elemento se llama 'cliente'
    for cliente in clientes:
        Cliente.objects.create(**cliente)
        # El operador ** descompone el diccionario para pasarlo como argumentos nombrados:

    """
        Cliente.objects.create(**cliente)
        Hace dos cosas internamente:

        Crea una instancia del modelo Cliente con los datos.

        Llama automáticamente a .save() para guardarlo en la base de datos.

        Lo mismo para el resto
    """

    
    for empleado in empleados:
        Empleado.objects.create(**empleado)

    for coordinador in coordinadores:
        Coordinador.objects.create(**coordinador)   
    
    for servicio in servicios:
        Servicio.objects.create(**servicio)

    # Crear las reservas con los objetos correctos
    reservas = [
        {
            "fecha_servicio": "2023-10-01 10:00:00",
            "cliente": Cliente.objects.get(pk=1),
            "empleado": Empleado.objects.get(pk=2),
            "coordinador": Coordinador.objects.get(pk=3),
            "servicio": Servicio.objects.get(pk=3),
            "total_precio": 1000,
        },
        {
            "fecha_servicio": "2026-10-01 10:00:00",
            "cliente": Cliente.objects.get(pk=4),
            "empleado": Empleado.objects.get(pk=4),
            "coordinador": Coordinador.objects.get(pk=4),
            "servicio": Servicio.objects.get(pk=1),
            "total_precio": 1000,
        },
    ]

    for reserva in reservas:
        ReservaDeServicio.objects.create(
            fecha_servicio=reserva["fecha_servicio"],
            cliente=reserva["cliente"],
            servicio=reserva["servicio"],
            empleado=reserva["empleado"],
            coordinador=reserva["coordinador"],
            total_precio=reserva["total_precio"],
        )


    print("Base de datos de ejemplo creada con éxito.")
    print("Usuario con permisos creado: id: admin1 | pass: admin123 ")

