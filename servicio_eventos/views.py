from django.shortcuts import render

""" views.py 

Toda la logica como intermediario entre el modelo y la vista se encuentra en este archivo.


"""
def view_home(request):
    return render(request, "servicio_eventos/home.html")


#region de funciones para CRUD de clientes, empleados, coordinadores y servicios

from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ClienteForm, EmpleadoForm, CoordinadorForm, ServicioForm
from .models import Cliente, Empleado, Coordinador, Servicio

# ===================   CRUD FORMULARIO      ========================
# ===================   CRUD : Crear, Leer, Actualizar, Borrar  ========================

# ===================   CLIENTES        ========================

class ClienteFormView(FormView):
    template_name = "servicio_eventos/register_clients.html"
    form_class = ClienteForm
    success_url = reverse_lazy("list_services")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# ===================   EMPLEADOS       ========================
# ===================   COORDINADORES   ========================
# ===================   SERVICIOS       ========================

## Crear
class ServicioFormView(FormView):
    template_name = "servicio_eventos/load_services.html"
    form_class = ServicioForm
    success_url = reverse_lazy("load_services")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
## Leer 
class SerivicioListView(ListView):
    queryset = Servicio.objects.all()
    template_name = "servicio_eventos/services.html"
    context_object_name = "services"



#endregion