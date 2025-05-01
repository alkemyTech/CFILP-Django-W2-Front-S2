# App de Reservas para Eventos
Este proyecto consiste en una aplicación web desarrollada con Python y Django, orientada a la gestión de reservas para eventos. Está diseñada para mejorar la eficiencia, trazabilidad y automatización del proceso de reserva en instituciones educativas, centros culturales u organizaciones similares.

## 🚀 Objetivo
El objetivo principal es ofrecer una herramienta digital que permita a usuarios reservar espacios físicos o eventos, visualizar disponibilidad en tiempo real y generar reportes automatizados, optimizando la planificación y administración institucional.

## 🗺️ Funcionalidades
Registro y autenticación de usuarios

Panel de administrador con control total sobre usuarios, eventos y reservas

Gestión de reservas: creación, modificación y cancelación

Visualización de calendario y disponibilidad en tiempo real

Notificaciones por correo electrónico

Generación de reportes de uso y estadísticas

## 🕊️ Público objetivo
Estudiantes, docentes y personal administrativo de instituciones educativas

Organizadores de eventos en centros comunitarios o espacios culturales

## ✨ Tecnologías utilizadas
Lenguaje de programación: Python 3.x

Framework web: Django

Base de datos: SQLite (en desarrollo) / PostgreSQL (para producción)

Frontend: HTML5, CSS3, JavaScript (Bootstrap opcional)

Control de versiones: Git

Otros: Django Admin, autenticación integrada

## 📄 Módulos clave
Usuarios y roles: autenticación, permisos y administración.

Reservas: lógica de negocio, conflictos de horario, validaciones.

Calendario: disponibilidad visual en interfaz de usuario.

Reportes: exportación de datos en PDF o Excel (opcional).

Notificaciones: confirmaciones automáticas vía email.

## 📋 Requisitos del sistema
- ✅ Python 3.8+
- ✅ Django 4.x
- ✅ pip, virtualenv
- ✅ Navegador moderno

## 💻 Instalación

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install djangorestframework 
pip install django-widget-tweaks
pip install pytz
python manage.py migrate
python manage.py runserver
```

## ⚡︎ Estado del proyecto
En etapa de desarrollo inicial. Se cuenta con un modelo funcional mínimo viable (MVP) y estructura base del backend. Se planea avanzar hacia integración de calendario dinámico, interfaz gráfica más amigable y despliegue en la nube.

## 🏛️ Autor
Proyecto desarrollado como caso de negocio académico. Responsable: [Nombre del desarrollador o institución].