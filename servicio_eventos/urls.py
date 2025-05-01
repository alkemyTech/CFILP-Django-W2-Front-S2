from django.urls import path
from .views import view_home
from .views import (ClienteFormView,
                    SerivicioListView,
                    ReservaDeServicioFormView,
                    ReservaDeServicioRealizadosView)

from .login import signup_view, login_view, logout_view


urlpatterns = [
    path('',login_view,name='login'), # Login
    path("signup/",signup_view,name="signup"),
    path("logout/",logout_view,name="logout"),

    path('home/',view_home,name='home'), 

    # ===================== URLS CRUD ====================
    # ===================== CLIENTES ====================
    path("register_clients/",ClienteFormView.as_view(),name="register_clients"),
    # ===================== EMPLEADOS ====================
    # ===================== COORDINADORES ====================
    # ===================== SERVICIOS ====================
    path("services/",SerivicioListView.as_view(),name="services"),
    path("load_services/",ReservaDeServicioFormView.as_view(),name="load_services"),
      # ===================== SERVICIOS REALIZADOS ====================
    path("list_services/",ReservaDeServicioRealizadosView.as_view(),name="list_services"),
]


