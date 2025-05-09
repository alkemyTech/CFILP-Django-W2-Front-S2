from django.shortcuts import render

""" views.py 

Toda la logica como intermediario entre el modelo y la vista se encuentra en este archivo.


"""
def view_home(request):
    # Ales comento 
    return render(request, "servicio_eventos/home.html")

#==================================================================================
# Para proteger la pagina, importo el decorador login_required
from django.contrib.auth.decorators import login_required
# method_decorator es para usar decoradores en CBV (Class Based Views)
from django.utils.decorators import method_decorator

# Mixin base para requerir login
class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige al login (asegúrate de que 'login' sea el nombre de tu URL de login)
#==================================================================================

#region de funciones para CRUD de clientes, empleados, coordinadores y servicios

from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, EmpleadoForm, CoordinadorForm, ReservaDeServicioForm
from .models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio

# ===================   CRUD FORMULARIO      ========================
# ===================   CRUD : Crear, Leer, Actualizar, Borrar  ========================

# ===================   CLIENTES        ========================

## Crear
class ClienteFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_clients.html"
    form_class = ClienteForm
    success_url = reverse_lazy("register_clients")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

## Leer
class ClienteListView(LoginRequiredMixin,ListView):
    queryset = Cliente.objects.filter(activo = True)
    template_name = "servicio_eventos/list_clients.html"
    context_object_name = "list_clients"

## Actualizar
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "servicio_eventos/register_clients.html"
    success_url = reverse_lazy("list_clients")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
## Borrar
""" QUEDA IMPLEMENTAR """


# ===================   EMPLEADOS       ========================

##Crear
class EmpleadoFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_employees.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("home")

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

## Leer
class EmpleadoListView(LoginRequiredMixin,ListView):
    queryset = Empleado.objects.filter(activo = True)
    template_name = "servicio_eventos/list_employees.html"
    context_object_name = "list_employees"

## Actualizar
""" QUEDA IMPLEMENTAR """
## Borrar
""" QUEDA IMPLEMENTAR """

# ===================   COORDINADORES   ========================

## Crear
class CoordinadorFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_coordinador.html"
    form_class = CoordinadorForm
    success_url = reverse_lazy("register_coordinadores")

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
## Leer
class CoordinadorListView(LoginRequiredMixin,ListView):
    queryset = Coordinador.objects.filter(activo = True)
    template_name = "servicio_eventos/list_coordinadores.html"
    context_object_name = "list_coordinadores"


## Actualizar
""" QUEDA IMPLEMENTAR """
## Borrar
""" QUEDA IMPLEMENTAR """
# ===================   SERVICIOS       ========================



# CBV CLASES BASADAS EN VISTAS


## Crear
class ReservaDeServicioFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/load_services.html"
    form_class = ReservaDeServicioForm
    success_url = reverse_lazy("load_services")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
## Leer 
class SerivicioListView(LoginRequiredMixin,ListView):
    queryset = Servicio.objects.filter(activo = True)
    template_name = "servicio_eventos/services.html"
    context_object_name = "services"


## Actualizar
""" QUEDA IMPLEMENTAR """
## Borrar
""" QUEDA IMPLEMENTAR """

# ===================   SERVICIOS REALIZADOS      ========================

from pytz import timezone as pytz_timezone
from django.utils import timezone

## Crear
class ReservaDeServicioRealizadosView(LoginRequiredMixin,ListView):
    queryset = ReservaDeServicio.objects.all()
    template_name = "servicio_eventos/list_services.html"
    context_object_name = "list_services"
    
    def get_queryset(self):
       hora_ar = timezone.now().astimezone(pytz_timezone("America/Argentina/Buenos_Aires")).date()
       servicios = ReservaDeServicio.objects.all()
       for s in servicios:
           fecha_servicio = s.fecha_servicio.astimezone(pytz_timezone("America/Argentina/Buenos_Aires")).date()
           if fecha_servicio < hora_ar:
               s.status = "Finalizado"
           elif fecha_servicio == hora_ar:
               s.status = "En curso hoy"
           else:
               s.status = "Pendiente"
       return servicios
    # Usamos select_related para obtener las relaciones de ForeignKey en una sola consulta

## Leer
""" QUEDA IMPLEMENTAR """
## Actualizar
""" QUEDA IMPLEMENTAR """
## Borrar
""" QUEDA IMPLEMENTAR """



#endregion



