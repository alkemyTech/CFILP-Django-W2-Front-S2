from django.contrib import admin
from .models import *
from public.models import SolicitudCotizacion

# Creamos super usuario para el admin:
# ID: admin 
# Pass: admin123

# Usuarios normales para inicio de sesion:
# ID: joa pass: joaquin1

class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('nombre', 'apellido', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ('activo',)

class EmpleadoAdmin(admin.ModelAdmin):
    model = Empleado
    list_display = ('nombre', 'apellido', 'numero_legajo', 'activo')
    search_fields = ('nombre', 'apellido', 'numero_legajo')
    list_filter = ('activo',)


class CoordinadorAdmin(admin.ModelAdmin):
    model = Coordinador
    list_display = ('nombre', 'apellido', 'numero_documento', 'fecha_alta', 'activo')
    search_fields = ('nombre', 'apellido', 'numero_documento')
    list_filter = ('activo', 'fecha_alta')


class ServicioAdmin(admin.ModelAdmin):
    model = Servicio
    list_display = ('nombre', 'precio', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo',)


class ReservaDeServicioAdmin(admin.ModelAdmin):
    model = ReservaDeServicio


admin.site.register(Cliente,ClienteAdmin) 
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Coordinador,CoordinadorAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(ReservaDeServicio,ReservaDeServicioAdmin)

@admin.register(SolicitudCotizacion)
class SolicitudCotizacionAdmin(admin.ModelAdmin):
    model = SolicitudCotizacion 
    list_display = (
        'get_servicio_display',
        'nombre', 
        'apellido', 
        'email', 
        'telefono', 
        'get_medio_preferido_contacto_display',
        'fecha_evento', 
        'cantidad_invitados',
        'presupuesto_estimado'
    )

    search_fields = (
        'nombre', 
        'apellido', 
        'email', 
        'telefono', 
        'servicio__nombre',
        'otro_tipo_evento'
    )

    list_filter = (
        'fecha_evento', 
        'medio_preferido_contacto',
        'servicio',
    )

    ordering = ('-fecha_evento',)

    def get_servicio_display(self, obj):
        if obj.servicio:
            display_text = str(obj.servicio) # Asume que el __str__ del modelo Servicio devuelve el nombre
            if obj.otro_tipo_evento:
                display_text += f" (Otro: {obj.otro_tipo_evento})"
            return display_text
        elif obj.otro_tipo_evento:
            return f"Otro: {obj.otro_tipo_evento}"
        return "N/A"
    get_servicio_display.short_description = 'Tipo de Evento' # Nombre de la columna

    fields = (
        ('servicio', 'otro_tipo_evento'), 
        ('nombre', 'apellido'),
        ('email', 'telefono'),
        'medio_preferido_contacto',
        ('fecha_evento', 'hora_evento'),
        'cantidad_invitados',
        'locacion_evento', 
        'direccion_evento',
        'presupuesto_estimado',
        'comentarios_adicionales_servicios',
        'como_nos_conocio'
    )


from django.contrib import admin
# Asumiendo que Proveedor y NuevoProveedor están en servicio_eventos.models
# Si los moviste a public/models.py, cambia la importación a:
# from .models import Proveedor, NuevoProveedor
from servicio_eventos.models import Proveedor, NuevoProveedor 

# Admin para el modelo Proveedor (los proveedores ya validados y activos)
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 
        'apellido', 
        'rubro', 
        'email', 
        'telefono', 
        'ciudad', 
        'provincia', 
        'activo'
    )
    search_fields = (
        'nombre', 
        'apellido', 
        'numero_documento', 
        'rubro', 
        'email', 
        'ciudad', 
        'provincia'
    )
    list_filter = (
        'activo', 
        'rubro', 
        'provincia', 
        'ciudad'
    )
    ordering = ('apellido', 'nombre')
    
    fieldsets = (
        ('Información Personal', {
            'fields': (('nombre', 'apellido'), 'numero_documento', ('email', 'telefono'))
        }),
        ('Detalles del Proveedor', {
            'fields': ('rubro', 'activo')
        }),
        ('Ubicación', {
            'fields': ('direccion', ('ciudad', 'provincia'), ('codigo_postal', 'pais'))
        }),
    )
    # Si quieres añadir acciones personalizadas, como "Desactivar seleccionados"
    # actions = ['desactivar_proveedores']

    # def desactivar_proveedores(self, request, queryset):
    #     queryset.update(activo=False)
    # desactivar_proveedores.short_description = "Marcar proveedores seleccionados como inactivos"

# Admin para el modelo NuevoProveedor (solicitudes de nuevos proveedores pendientes de validación)
@admin.register(NuevoProveedor)
class NuevoProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 
        'apellido', 
        'rubro', 
        'email', 
        'telefono', 
        'ciudad', 
        'provincia', 
        'activo' # Podrías querer filtrar por 'activo=False' para ver los pendientes
    )
    search_fields = (
        'nombre', 
        'apellido', 
        'numero_documento', 
        'rubro', 
        'email'
    )
    list_filter = (
        'activo', # Muy útil para separar los ya procesados/aprobados de los nuevos
        'rubro', 
        'provincia', 
        'ciudad',
    )
    ordering = ('-id',) # Mostrar los más recientes primero

    # Acciones personalizadas para el admin
    actions = ['marcar_como_activo_y_crear_proveedor', 'marcar_como_inactivo']

    # Definición de campos en el formulario de detalle/edición
    # Similar a ProveedorAdmin, pero podrías querer todos los campos visibles para revisión
    fields = (
        ('nombre', 'apellido'), 
        'numero_documento', 
        ('email', 'telefono'),
        'rubro', 
        'direccion', 
        ('ciudad', 'provincia'), 
        ('codigo_postal', 'pais'),
        'activo' # Permitir marcar como activo/inactivo directamente
    )

    def marcar_como_activo_y_crear_proveedor(self, request, queryset):
        proveedores_creados_count = 0
        for nuevo_proveedor_solicitud in queryset:
            if not nuevo_proveedor_solicitud.activo: # Solo procesar si no está ya activo
                # Crear una instancia de Proveedor con los datos de NuevoProveedor
                proveedor_nuevo, created = Proveedor.objects.get_or_create(
                    numero_documento=nuevo_proveedor_solicitud.numero_documento, # Usar un campo único para evitar duplicados
                    defaults={
                        'nombre': nuevo_proveedor_solicitud.nombre,
                        'apellido': nuevo_proveedor_solicitud.apellido,
                        'rubro': nuevo_proveedor_solicitud.rubro,
                        'direccion': nuevo_proveedor_solicitud.direccion,
                        'ciudad': nuevo_proveedor_solicitud.ciudad,
                        'provincia': nuevo_proveedor_solicitud.provincia,
                        'pais': nuevo_proveedor_solicitud.pais,
                        'codigo_postal': nuevo_proveedor_solicitud.codigo_postal,
                        'email': nuevo_proveedor_solicitud.email,
                        'telefono': nuevo_proveedor_solicitud.telefono,
                        'activo': True # El nuevo proveedor se crea como activo
                    }
                )
                if created:
                    # Marcar la solicitud de NuevoProveedor como activa (procesada)
                    nuevo_proveedor_solicitud.activo = True
                    nuevo_proveedor_solicitud.save()
                    proveedores_creados_count += 1
                else:
                    # Si ya existe un Proveedor con ese DNI, solo marcamos la solicitud como procesada
                    nuevo_proveedor_solicitud.activo = True 
                    nuevo_proveedor_solicitud.save()
                    self.message_user(request, f"El proveedor {proveedor_nuevo} ya existía. La solicitud ha sido marcada como procesada.", level='WARNING')

        if proveedores_creados_count > 0:
            self.message_user(request, f"{proveedores_creados_count} nuevos proveedores han sido creados y activados exitosamente.")
    marcar_como_activo_y_crear_proveedor.short_description = "Aprobar seleccionados (marcar activo y crear Proveedor)"

    def marcar_como_inactivo(self, request, queryset):
        updated_count = queryset.update(activo=False)
        self.message_user(request, f"{updated_count} solicitudes de proveedores han sido marcadas como inactivas/rechazadas.")
    marcar_como_inactivo.short_description = "Rechazar seleccionados (marcar como inactivo)"
