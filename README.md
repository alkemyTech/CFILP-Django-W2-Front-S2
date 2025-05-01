# App de Reservas para Eventos
Este proyecto consiste en una aplicación web desarrollada con Python y Django, orientada a la gestión de reservas para eventos. Está diseñada para mejorar la eficiencia, trazabilidad y automatización del proceso de reserva de eventos para instituciones educativas, centros culturales u organizaciones similares.

## 🚀 Objetivo
El objetivo principal es ofrecer una herramienta digital que permita a los empleados de una institucion o empresa, reservar eventos, visualizar disponibilidad en tiempo real, optimizando la planificación y administración institucional.

## 🗺️ Funcionalidades
Registro y autenticación de usuarios

Panel de administrador con control total sobre usuarios, eventos, reservas y clientes

Gestión de reservas: creación, modificación y cancelación

## 🕊️ Público objetivo
Estudiantes, docentes y personal administrativo de instituciones

Organizadores de eventos en centros comunitarios o espacios culturales

## ✨ Tecnologías utilizadas
Lenguaje de programación: Python 3.x

Framework web: Django

Base de datos: SQLite (en desarrollo)

Frontend: HTML5, CSS3, JavaScript, Bootstrap

Control de versiones: Git

Otros: Django Admin, autenticación integrada

## 📄 Módulos clave
Usuarios y roles: autenticación, permisos y administración.

Reservas: lógica de negocio, conflictos de horario, validaciones.

Calendario: disponibilidad visual en interfaz de usuario.

## 📋 Requisitos del sistema
- ✅ Python 3.8+
- ✅ Django 4.x
- ✅ pip, virtualenv
- ✅ Navegador moderno

## 💻 Instalación

```bash
git clone https://github.com/alkemyTech/CFILP-Django-W2-Front-S2
cd repositorio
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install djangorestframework 
pip install django-widget-tweaks
pip install pytz
python manage.py migrate
python manage.py runserver
```

## 🏛️ Autor
Proyecto desarrollado como caso de negocio académico. Responsables: Alesandro Maldonado, Joaquin Hernandez, Romina Isaia, Nicolas Lobos.