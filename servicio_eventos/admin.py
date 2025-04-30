from django.contrib import admin
from .models import Cliente, Empleado, Coordinador, Servicio


# Creamos super usuario para el admin:
# ID: admin 
# Pass: admin123


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


admin.site.register(Cliente,ClienteAdmin) 
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Coordinador,CoordinadorAdmin)
admin.site.register(Servicio,ServicioAdmin)