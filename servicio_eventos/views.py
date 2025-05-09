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
from .forms import ClienteForm, EmpleadoForm, CoordinadorForm, ReservaDeServicioForm, ServiciosForm
from .models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio
from django.contrib import messages


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
        messages.success(self.request, "¡Cliente registrado con éxito!")
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
        cliente = form.save(commit=False)
        messages.success(self.request, f"¡Cliente '{cliente.nombre}' actualizado con éxito!")
        form.save()
        return super().form_valid(form)
    
## Borrar
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "servicio_eventos/delete_clients.html"
    success_url = reverse_lazy("list_clients")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_clients'] = Cliente.objects.filter(activo=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False  # Cambia el estado a inactivo
        self.object.save()
        return redirect(self.success_url)


# ===================   EMPLEADOS       ========================

##Crear
class EmpleadoFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_employees.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("register_employees")

    def form_valid(self,form):
        form.save()
        messages.success(self.request, "¡Empleado registrado con éxito!")
        return super().form_valid(form)

## Leer
class EmpleadoListView(LoginRequiredMixin,ListView):
    queryset = Empleado.objects.filter(activo = True)
    template_name = "servicio_eventos/list_employees.html"
    context_object_name = "list_employees"

## Actualizar
class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "servicio_eventos/register_employees.html"
    success_url = reverse_lazy("list_employees")

    def form_valid(self, form):
        empleado = form.save(commit=False)
        messages.success(self.request, f"¡Empleado '{empleado.nombre}' actualizado con éxito!")
        form.save()
        return super().form_valid(form)

## Borrar
class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = "servicio_eventos/delete_employees.html"
    success_url = reverse_lazy("list_employees")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_employees'] = Empleado.objects.filter(activo=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False  # Cambia el estado a inactivo
        self.object.save()
        return redirect(self.success_url)

# ===================   COORDINADORES   ========================

## Crear
class CoordinadorFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_coordinador.html"
    form_class = CoordinadorForm
    success_url = reverse_lazy("register_coordinadores")

    def form_valid(self,form):
        form.save()
        messages.success(self.request, "¡Coordinador creado con éxito!")
        return super().form_valid(form)
    
## Leer
class CoordinadorListView(LoginRequiredMixin,ListView):
    queryset = Coordinador.objects.filter(activo = True)
    template_name = "servicio_eventos/list_coordinadores.html"
    context_object_name = "list_coordinadores"

## Actualizar
class CoordinadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Coordinador
    form_class = CoordinadorForm
    template_name = "servicio_eventos/register_coordinador.html"
    success_url = reverse_lazy("list_coordinadores")

    def form_valid(self, form):
        coordinador = form.save(commit=False)
        messages.success(self.request, f"¡Coordinador '{coordinador.nombre}' actualizado con éxito!")
        form.save()
        return super().form_valid(form)
## Borrar
class CoordinadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Coordinador
    template_name = "servicio_eventos/delete_coordinadores.html"
    success_url = reverse_lazy("list_coordinadores")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_coordinadores'] = Coordinador.objects.filter(activo=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False  # Cambia el estado a inactivo
        self.object.save()
        return redirect(self.success_url)


# ===================   RESERVA SERVICIOS       ========================
## Crear
class ReservaDeServicioFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/load_services.html"
    form_class = ReservaDeServicioForm
    success_url = reverse_lazy("load_services")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Reserva creada con éxito!")
        return super().form_valid(form)
    
## Leer
from pytz import timezone as pytz_timezone
from django.utils import timezone

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

## Actualizar
class ReservaServicioUpdateView(LoginRequiredMixin, UpdateView):  
    model = ReservaDeServicio
    form_class = ReservaDeServicioForm
    template_name = "servicio_eventos/load_services.html"
    success_url = reverse_lazy("services")

    def form_valid(self, form):
        reserva = form.save(commit=False)
        messages.success(self.request, f"¡Reserva de: '{reserva.cliente.nombre}' para '{reserva.servicio.nombre}' actualizado con éxito!")
        form.save()
    
        return super().form_valid(form)

## Borrar
class ReservaServicioDeleteView(LoginRequiredMixin, DeleteView):
    model = ReservaDeServicio
    template_name = "servicio_eventos/delete_services.html"
    success_url = reverse_lazy("list_services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_services'] = ReservaDeServicio.objects.values('fecha_servicio')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

# ===================   SERVICIOS DISPONIBLES      ========================

## Crear
class ServiciosFormView(LoginRequiredMixin,FormView):
    template_name = "servicio_eventos/register_services.html"
    form_class = ServiciosForm
    success_url = reverse_lazy("register_services")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Servicio creado con éxito!")
        return super().form_valid(form)
## Leer 
class SerivicioListView(LoginRequiredMixin,ListView):
    queryset = Servicio.objects.filter(activo = True)
    template_name = "servicio_eventos/services.html"
    context_object_name = "services"

## Actualizar  
class ServicioUpateView(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ServiciosForm
    template_name = "servicio_eventos/register_services.html"
    success_url = reverse_lazy("services")

    def form_valid(self, form):
        servicio = form.save(commit=False)
        messages.success(self.request, f"¡ervicio '{servicio.nombre}' actualizado con éxito!")
        form.save()
        return super().form_valid(form)

## Borrar
class ServicioDeleteView(LoginRequiredMixin, DeleteView):
    model = Servicio
    template_name = "servicio_eventos/borrar_services.html"
    success_url = reverse_lazy("services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Servicio.objects.filter(activo=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False  # Cambia el estado a inactivo
        self.object.save()
        return redirect(self.success_url)

#endregion



