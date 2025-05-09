from django.shortcuts import render
from servicio_eventos.models import Cliente, Servicio
from django.shortcuts import render, get_object_or_404

def view_casa(request):
    return render(request, "public/casa.html")

def view_cotizacion(request):
    evento = None

    # Verificar si la solicitud es GET y si existe el parámetro 'evento_id'
    if request.method == "GET":
        evento_id = request.GET.get("evento_id")
        if evento_id:
            evento = get_object_or_404(Servicio, id=evento_id)  # Obtener evento por su ID
        servicios = Servicio.objects.all()  # Obtener los servicios desde la base de datos

        return render(request, "public/cotizacion.html", {
            "evento": evento,
            "servicios": servicios
        })

    # Verificar si la solicitud es POST
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email") or request.data.get('email')
        telefono = request.POST.get("telefono")
        Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, activo=True)

        print("Se hizo un POST")
        # Aquí puedes agregar la lógica para guardar los datos o enviar un correo

    return render(request, "public/cotizacion.html")
    

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