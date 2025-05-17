from django import forms
from .models import SolicitudCotizacion 
from servicio_eventos.models import Servicio

class SolicitudCotizacionForm(forms.ModelForm):
    terminos_condiciones = forms.BooleanField(
        label="Acepto los Términos y Condiciones y la Política de Privacidad.",
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-checkbox h-5 w-5 rounded text-pink-500 focus:ring-pink-400 border-gray-300 shadow-sm'})
    )
    OPCIONES_COMO_NOS_CONOCIO = [
        ('', 'Selecciona una opción...'),
        ('redes_sociales', 'Redes Sociales (Facebook, Instagram, etc.)'),
        ('busqueda_google', 'Búsqueda en Google'),
        ('recomendacion_amigo_familiar', 'Recomendación de amigo/familiar'),
        ('publicidad_online', 'Publicidad Online'),
        ('evento_anterior', 'Asistí a un evento organizado por ustedes'),
        ('otro_medio', 'Otro Medio')
    ]
    como_nos_conocio = forms.ChoiceField(
        label="¿Cómo nos conociste?",
        choices=OPCIONES_COMO_NOS_CONOCIO,
        required=False,
        widget=forms.Select(attrs={'class': 'form-input-public'})
    )

    class Meta:
        model = SolicitudCotizacion
        fields = '__all__'

        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-input-public'}),
            'otro_tipo_evento': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': 'Ej: Fiesta de compromiso'}),
            'fecha_evento': forms.DateInput(attrs={'type': 'date', 'class': 'form-input-public'}),
            'hora_evento': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input-public'}),
            'cantidad_invitados': forms.NumberInput(attrs={'class': 'form-input-public', 'placeholder': 'Ej: 50', 'min': '1'}),
            'locacion_evento': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': 'Ej: Hotel Lumière Plaza'}),
            'direccion_evento': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': 'Calle, Número, Ciudad'}),
            'presupuesto_estimado': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': 'Ej: $50.000 - $100.000 ARS'}),
            'comentarios_adicionales_servicios': forms.Textarea(attrs={'class': 'form-input-public', 'rows': 4, 'placeholder': 'Describe cualquier idea específica...'}),
            'nombre': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': 'Tu nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': 'Tu apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-input-public', 'placeholder': 'tu@email.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-input-public', 'placeholder': '+54 9 11 XXXX-XXXX', 'type': 'tel'}),
            'medio_preferido_contacto': forms.Select(attrs={'class': 'form-input-public'}),
            'como_nos_conocio': forms.Select(attrs={'class': 'form-input-public'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'servicio' in self.fields:
            self.fields['servicio'].queryset = Servicio.objects.filter(activo=True).order_by('nombre')
            self.fields['servicio'].empty_label = "Selecciona el tipo de evento..."

        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = 'required'
       