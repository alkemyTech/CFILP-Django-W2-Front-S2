from django.forms import ModelForm
from .models import Cliente,Servicio,Coordinador,Empleado,ReservaDeServicio
from django import forms


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ReservaDeServicioForm(forms.ModelForm):
    class Meta:
        model = ReservaDeServicio
        exclude = ['fecha_reserva']  # no editable
        widgets = {
            'fecha_servicio': forms.DateTimeInput(attrs={
                'class': 'form-control', 
                'type': 'datetime-local'
            }),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'coordinador': forms.Select(attrs={'class': 'form-control'}),
            'total_precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CoordinadorForm(ModelForm):
    class Meta:
        model = Coordinador
        fields = '__all__'


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


