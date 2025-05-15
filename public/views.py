from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # Para mostrar mensajes al usuario (opcional)

# Asumo que el modelo Servicio está en la app 'servicio_eventos'
from servicio_eventos.models import Servicio, NuevoProveedor # Asegúrate que estos modelos existan en servicio_eventos/models.py
# Asumo que SolicitudCotizacion y SolicitudCotizacionForm están en la app 'public'
from .models import SolicitudCotizacion # ¡Asegúrate que este modelo exista en public/models.py!
from .forms import SolicitudCotizacionForm # ¡Asegúrate que este form exista en public/forms.py!

def view_casa(request):
    return render(request, "public/casa.html")

def view_cotizacion(request):
    servicios_obj = Servicio.objects.filter(activo=True).order_by('nombre')

    if request.method == 'POST':
        form = SolicitudCotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu solicitud de cotización ha sido enviada con éxito! Te contactaremos pronto.')
            return redirect('casa')
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, revisa los campos marcados.')
    else:  # Método GET
        initial_data = {}
        evento_id_get = request.GET.get('evento_id')
        if evento_id_get:
            try:
                evento_obj = get_object_or_404(Servicio, id=evento_id_get)
                initial_data['servicio'] = evento_obj
            except Servicio.DoesNotExist:
                messages.warning(request, 'El servicio seleccionado para cotizar no fue encontrado.')
        form = SolicitudCotizacionForm(initial=initial_data)

    context = {
        'form': form,
        'servicios': servicios_obj
    }
    return render(request, "public/cotizacion.html", context)


def view_cumple(request):
    return render(request, "public/cumple.html")

def view_boda(request):
    return render(request, "public/boda.html")

def view_ejecutivo(request):
    return render(request, "public/ejecutivo.html")

def view_politicas(request):
    return render(request, "public/politicas.html")

def view_terminos(request):
    return render(request, "public/terminos.html")

def view_testimonios(request):
    return render(request, "public/testimonios.html")

def view_agregar_testimonio(request):
    return render(request, "public/agregar_testimonio.html")

def view_catering(request):
    return render(request, "public/catering.html")

def view_deco(request):
    return render(request, "public/deco.html")

def view_dj(request):
    return render(request, "public/dj.html")

def view_foto_artistica(request):
    return render(request, "public/foto_artistica.html")

def view_galeria_fotos_boda(request):
    return render(request, "public/galeria_fotos_boda.html")

def view_lugares(request):
    return render(request, "public/lugares.html")

from django.shortcuts import render, redirect

def view_new_proveedor(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        numero_documento = request.POST.get("numero_documento")
        rubro = request.POST.get("rubro")
        direccion = request.POST.get("direccion")
        ciudad = request.POST.get("ciudad")
        provincia = request.POST.get("provincia")
        pais = request.POST.get("pais")
        codigo_postal = request.POST.get("codigo_postal")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")

        NuevoProveedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            numero_documento=numero_documento,
            rubro=rubro,
            direccion=direccion,
            ciudad=ciudad,
            provincia=provincia,
            pais=pais,
            codigo_postal=codigo_postal,
            activo=True
        )

        print("Se hizo un POST")
        return redirect("/public/new_provider")  # o la URL que corresponda

    return render(request, "public/new_provider.html")

