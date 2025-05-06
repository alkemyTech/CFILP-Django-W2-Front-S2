from django.shortcuts import render
from datetime import datetime

def view_home(request):
    servicios = [
        {"titulo": "Consultoría en Ventas", "descripcion": "Identificamos oportunidades de mejora."},
        {"titulo": "Gestión de Clientes", "descripcion": "Optimización de relaciones comerciales."},
        {"titulo": "Capacitación de Equipos", "descripcion": "Formación para equipos de venta."},
    ]
    contexto = {
        "titulo_pagina": "Inicio | Mi Empresa",
        "nombre_empresa": "Mi Empresa",
        "descripcion_empresa": "Soluciones efectivas para ventas",
        "quienes_somos": "Somos expertos en ventas adaptadas a tu negocio.",
        "servicios": servicios,
        "llamado_accion_texto": "Impulsa tus ingresos con nuestra ayuda.",
        "anio_actual": datetime.now().year,
        "email_contacto": "info@miempresa.com",
        "telefono_contacto": "+54 11 1234-5678",
    }
    return render(request, "public/home.html", contexto)
