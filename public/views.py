from django.shortcuts import render
from servicio_eventos.models import Cliente

def view_casa(request):
    return render(request, "public/casa.html")

def view_cotizacion(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        Cliente.objects.create(nombre=nombre, apellido=apellido, activo=True)
        
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