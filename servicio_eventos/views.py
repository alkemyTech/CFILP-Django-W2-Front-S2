from django.shortcuts import render

""" views.py 

Toda la logica como intermediario entre el modelo y la vista se encuentra en este archivo.


"""
def view_home(request):
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
    
#==================================================================================

#region de funciones para CRUD de clientes, empleados, coordinadores y servicios

from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, EmpleadoForm, CoordinadorForm, ReservaDeServicioForm
from .models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio

# ===================   CRUD FORMULARIO      ========================
# ===================   CRUD : Crear, Leer, Actualizar, Borrar  ========================

# ===================   CLIENTES        ========================

class ClienteFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_clients.html"
    form_class = ClienteForm
    success_url = reverse_lazy("register_clients")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

# ===================   EMPLEADOS       ========================
# ===================   COORDINADORES   ========================
# ===================   SERVICIOS       ========================

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
    queryset = Servicio.objects.all()
    template_name = "servicio_eventos/services.html"
    context_object_name = "services"


# ===================   SERVICIOS REALIZADOS      ========================
class ReservaDeServicioRealizadosView(LoginRequiredMixin,ListView):
    queryset = ReservaDeServicio.objects.all()
    template_name = "servicio_eventos/list_services.html"
    context_object_name = "list_services"
    
    # Usamos select_related para obtener las relaciones de ForeignKey en una sola consulta

#endregion