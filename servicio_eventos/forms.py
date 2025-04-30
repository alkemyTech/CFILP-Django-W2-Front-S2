from django.forms import ModelForm
from .models import Cliente,Servicio,Coordinador,Empleado,ReservaDeServicio
# Forms.py 


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio']


class CoordinadorForm(ModelForm):
    class Meta:
        model = Coordinador
        fields = '__all__'


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


