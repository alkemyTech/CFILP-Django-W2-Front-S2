from django.urls import path
from .views import view_home
from .views import (ClienteFormView,
                    ClienteListView,
                    ClienteUpdateView,
                    ClienteDeleteView,
                    EmpleadoFormView,
                    EmpleadoListView,
                    EmpleadoUpdateView,
                    EmpleadoDeleteView,
                    CoordinadorFormView,
                    CoordinadorListView,
                    CoordinadorUpdateView,
                    CoordinadorDeleteView,
                    ReservaDeServicioFormView,
                    ReservaServicioUpdateView,
                    ReservaDeServicioRealizadosView,
                    ReservaServicioDeleteView,
                    ServiciosFormView,
                    SerivicioListView,
                    ServicioUpateView,
                    ServicioDeleteView,
                    ProveedorFormView,
                    ProveedorListView,
                    ProveedorUpdateView,
                    ProveedorDeleteView)

from .login import signup_view, login_view, logout_view
from . import views


urlpatterns = [
    path('',login_view,name='login'), # Login
    path("signup/",signup_view,name="signup"),
    path("logout/",logout_view,name="logout"),

    path('home/',view_home,name='home'), 
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),

    # ===================== URLS CRUD ====================
    # ===================== CLIENTES ====================
    path("register_clients/",ClienteFormView.as_view(),name="register_clients"),                        #CREAR
    path("list_clients/",ClienteListView.as_view(),name="list_clients"),                                #LEER 
    path("update_clients/<int:pk>/",ClienteUpdateView.as_view(),name="update_clients"),                 #ACTUALIZAR
    path("delete_clients/<int:pk>/",ClienteDeleteView.as_view(),name="delete_clients"),                 #BORRAR

    # ===================== EMPLEADOS ====================
    path("register_employees/",EmpleadoFormView.as_view(),name="register_employees"),                   #CREAR
    path("list_employees/",EmpleadoListView.as_view(),name="list_employees"),                           #LEER
    path("update_employees/<int:pk>/",EmpleadoUpdateView.as_view(),name="update_employees"),            #ACTUALIZAR
    path("delete_employees/<int:pk>/",EmpleadoDeleteView.as_view(),name="delete_employees"),            #BORRAR

    # ===================== COORDINADORES ====================
    path("register_coordinadores/",CoordinadorFormView.as_view(),name="register_coordinadores"),            #CREAR
    path("list_coordinadores/",CoordinadorListView.as_view(),name="list_coordinadores"),                    #LEER
    path("update_coordinadores/<int:pk>/",CoordinadorUpdateView.as_view(),name="update_coordinadores"),     #ACTUALIZAR
    path("delete_coordinadores/<int:pk>/",CoordinadorDeleteView.as_view(),name="delete_coordinadores"),     #BORRAR

    # ===================== RESERVA SERVICIOS ====================
    path("load_services/",ReservaDeServicioFormView.as_view(),name="load_services"),                    #CREAR
    path("list_services/",ReservaDeServicioRealizadosView.as_view(),name="list_services"),              #LEER
    path("update_services/<int:pk>/",ReservaServicioUpdateView.as_view(),name="update_services"),       #ACTUALIZAR
    path("delete_services/<int:pk>/",ReservaServicioDeleteView.as_view(),name="delete_services"),       #BORRAR
   
    # ===================== SERVICIOS DISPONIBLES ====================
    path("register_services/",ServiciosFormView.as_view(),name="register_services"),                    #CREAR
    path("services/",SerivicioListView.as_view(),name="services"),                                      #LEER  
    path("actualizar_services/<int:pk>/",ServicioUpateView.as_view(),name="actualizar_services"),       #ACTUALIZAR
    path("borrar_services/<int:pk>/",ServicioDeleteView.as_view(),name="borrar_services"),              #BORRAR

    # ===================== PROVEEDORES ====================
    path("register_providers/",ProveedorFormView.as_view(),name="register_providers"),                  #CREAR
    path("list_providers/",ProveedorListView.as_view(),name="list_providers"),                          #LEER
    path("update_providers/<int:pk>/",ProveedorUpdateView.as_view(),name="update_providers"),           #ACTUALIZAR
    path("delete_providers/<int:pk>/",ProveedorDeleteView.as_view(),name="delete_providers"),           #BORRAR
]


