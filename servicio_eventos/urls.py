from django.urls import path
from .views import view_home
from .views import (ClienteFormView,
                    ServicioFormView,SerivicioListView,)



urlpatterns = [
    path('home/',view_home,name='home'), 

    # ===================== URLS CRUD ====================
    # ===================== CLIENTES ====================
    path("register_clients/",ClienteFormView.as_view(),name="register_clients"),
    # ===================== EMPLEADOS ====================
    # ===================== COORDINADORES ====================
    # ===================== SERVICIOS ====================
    path("services/",SerivicioListView.as_view(),name="services"),
    path("load_services/",ServicioFormView.as_view(),name="load_services"),
    
    #path("list_services/",view_services,name="list_services"),
]


