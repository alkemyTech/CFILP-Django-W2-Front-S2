from django.urls import path
from .views import view_home
from .views import (ClienteFormView,
                    ClienteListView,
                    ClienteUpdateView,
                    SerivicioListView,
                    EmpleadoFormView,
                    EmpleadoListView,
                    CoordinadorFormView,
                    CoordinadorListView,
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
    path("register_clients/",ClienteFormView.as_view(),name="register_clients"), #CREAR
    path("list_clients/",ClienteListView.as_view(),name="list_clients"), #LEER 
    path("update_clients/<int:pk>/"",ClienteUpdateView.as_view(),name="update_clients"), #ACTUALIZAR
    # path("delete_clients/<int:pk>/",ClienteFormView.as_view(),name="delete_clients"), #BORRAR

    # ===================== EMPLEADOS ====================
    path("register_employees/",EmpleadoFormView.as_view(),name="register_employees"),   #CREAR
    path("list_employees/",EmpleadoListView.as_view(),name="list_employees"), #LEER

    # ===================== COORDINADORES ====================
    path("register_coordinadores/",CoordinadorFormView.as_view(),name="register_coordinadores"),    #CREAR
    path("list_coordinadores/",CoordinadorListView.as_view(),name="list_coordinadores"), #LEER

    # ===================== SERVICIOS ====================
     path("load_services/",ReservaDeServicioFormView.as_view(),name="load_services"),    #CREAR
    path("services/",SerivicioListView.as_view(),name="services"),  #LEER  
   
      # ===================== SERVICIOS REALIZADOS ====================
    path("list_services/",ReservaDeServicioRealizadosView.as_view(),name="list_services"),  #LEER
]


