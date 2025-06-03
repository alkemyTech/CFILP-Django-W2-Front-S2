from django.db import models
from servicio_eventos.models import Servicio

class SolicitudCotizacion(models.Model):
    MEDIOS_CONTACTO = [
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('llamada', 'Llamada Telefónica'),
    ]

    # Campos del Paso 1: Detalles de Tu Celebración
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    otro_tipo_evento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Otro Tipo de Evento (si aplica)")
    fecha_evento = models.DateField(verbose_name="Fecha Estimada del Evento")
    hora_evento = models.TimeField(blank=True, null=True, verbose_name="Hora Estimada del Evento")
    cantidad_invitados = models.PositiveIntegerField(verbose_name="Número Estimado de Invitados")
    locacion_evento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Lugar del Evento")
    direccion_evento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección del Evento")
    
    # Campos del Paso 2: Servicios Requeridos
    presupuesto_estimado = models.CharField(max_length=100, blank=True, null=True, verbose_name="Presupuesto Estimado")
    comentarios_adicionales_servicios = models.TextField(blank=True, null=True, verbose_name="Comentarios Adicionales sobre Servicios")

    # Campos del Paso 3: Datos de Contacto
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Solicitante")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Solicitante")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono / WhatsApp")
    medio_preferido_contacto = models.CharField(max_length=20, choices=MEDIOS_CONTACTO, default='whatsapp', verbose_name="Medio Preferido de Contacto")
    como_nos_conocio = models.CharField(max_length=100, blank=True, null=True, verbose_name="¿Cómo nos conoció?")

    def __str__(self):
        return f"Solicitud de {self.nombre} {self.apellido} para {self.servicio}"