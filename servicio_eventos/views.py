from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
from pytz import timezone as pytz_timezone
from public.models import SolicitudCotizacion 
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from .models import Cliente, Empleado, Coordinador, Servicio, ReservaDeServicio, Proveedor
from .forms import ClienteForm, EmpleadoForm, CoordinadorForm, ReservaDeServicioForm, ServiciosForm, ProveedorForm, NuevoProveedorForm


@login_required
def listar_solicitudes_publicas(request):
    solicitudes = SolicitudCotizacion.objects.all().order_by('-fecha_evento') 
    context = {
        'lista_de_solicitudes': solicitudes,
        'titulo_pagina': "Listado de Solicitudes de Cotización (Públicas)",
    }
    return render(request, 'servicio_eventos/solicitudes_publicas.html', context)

class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def view_home(request):
    return render(request, "servicio_eventos/home.html")

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

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


# ===================   RESERVA SERVICIOS       ================

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


# ===================   Proveedores       ========================

## Nuevo proveedor public
class NuevoProveedorFormView(LoginRequiredMixin, FormView):
    form_class = NuevoProveedorForm
    template_name = "public/new_provider.html"
    success_url = reverse_lazy("new_provider.html")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Solicitud de proveedor creada con éxito!")
        return super().form_valid(form)

## Crear
class ProveedorFormView(LoginRequiredMixin, FormView):
    form_class = ProveedorForm
    template_name = "servicio_eventos/register_providers.html"
    success_url = reverse_lazy("list_providers")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Proveedor creado con éxito!")
        return super().form_valid(form)

## Leer
class ProveedorListView(LoginRequiredMixin, ListView):
    queryset = Proveedor.objects.all()
    template_name = "servicio_eventos/list_providers.html"
    context_object_name = "list_providers"

## Actualizar
class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "servicio_eventos/register_providers.html"
    success_url = reverse_lazy("list_providers")

    def form_valid(self, form):
        proveedor = form.save(commit=False)
        messages.success(self.request, f"¡Proveedor '{proveedor.nombre}' actualizado con éxito!")
        form.save()
        return super().form_valid(form)

## Borrar
class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = "servicio_eventos/delete_providers.html"
    success_url = reverse_lazy("list_providers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_providers'] = Proveedor.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)