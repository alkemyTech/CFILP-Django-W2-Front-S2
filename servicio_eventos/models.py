from django.db import models

# Crate interfaces for implementing the switch activate method
class ISwitchActivate():
    def delete(self, using = None, keep_parents=False):
        self.activo = not self.activo
        self.save()


# Create your models here.
class Cliente(models.Model,ISwitchActivate):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Empleado(models.Model,ISwitchActivate):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Coordinador(models.Model,ISwitchActivate):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_documento = models.IntegerField()
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Servicio(models.Model,ISwitchActivate):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"


class ReservaDeServicio(models.Model):
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_servicio = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    total_precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva: {self.servicio} Coordinado por: {self.coordinador}"
    
    
"""class ServiciosRealizados(models.Model):
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_servicio = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE)
    total_precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva: {self.servicio} Coordinado por: {self.coordinador}"
    """