from django import forms
from .models import SolicitudCotizacion 
from servicio_eventos.models import Servicio # Asegúrate que este modelo exista en servicio_eventos/models.py
# Si el modelo Servicio está en otra app, ajústalo. Ej: from servicio_eventos.models import Servicio

class SolicitudCotizacionForm(forms.ModelForm):
    terminos_condiciones = forms.BooleanField(
        label="Acepto los Términos y Condiciones y la Política de Privacidad.",
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-checkbox rounded text-pink-500 focus:ring-pink-400 focus:ring-offset-0'})
    )
    class Meta:
        model = SolicitudCotizacion
        fields = '__all__'
        widgets = {
            'hora_evento': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'fecha_evento': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'servicio': forms.Select(attrs={'class': 'form-input-public'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicio.objects.filter(activo=True).order_by('nombre')
        self.fields['servicio'].empty_label = "Selecciona el tipo de evento..."