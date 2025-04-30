from django.contrib import admin
from .models import Cliente, Empleado, Coordinador, Servicio

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ('activo',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_legajo', 'activo')
    search_fields = ('nombre', 'apellido', 'numero_legajo')
    list_filter = ('activo',)

@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_documento', 'fecha_alta', 'activo')
    search_fields = ('nombre', 'apellido', 'numero_documento')
    list_filter = ('activo', 'fecha_alta')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo',)
