from django import forms
from .models import SolicitudCotizacion 
from servicio_eventos.models import Servicio # Asegúrate que este modelo exista en servicio_eventos/models.py
# Si el modelo Servicio está en otra app, ajústalo. Ej: from servicio_eventos.models import Servicio

class SolicitudCotizacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudCotizacion
        fields = '__all__'
        widgets = {
            'servicio': forms.Select(attrs={'class': 'form-input-public'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicio'].queryset = Servicio.objects.filter(activo=True).order_by('nombre')
        self.fields['servicio'].empty_label = "Selecciona el tipo de evento..."