from django.urls import path
from .views import view_home
from .views import (ClienteFormView,
                    SerivicioListView,
                    EmpleadoFormView,
                    CoordinadorFormView,
                    ReservaDeServicioFormView,
                    ReservaDeServicioRealizadosView)

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
    path("register_clients/",ClienteFormView.as_view(),name="register_clients"),
    # ===================== EMPLEADOS ====================
    path("register_employees/",EmpleadoFormView.as_view(),name="register_employees"),
    # ===================== COORDINADORES ====================
    path("register_coordinadores/",CoordinadorFormView.as_view(),name="register_coordinadores"),
    # ===================== SERVICIOS ====================
    path("load_services/",ReservaDeServicioFormView.as_view(),name="load_services"),
    path("services/",SerivicioListView.as_view(),name="services"),
      # ===================== SERVICIOS REALIZADOS ====================
    path("list_services/",ReservaDeServicioRealizadosView.as_view(),name="list_services"),
]


