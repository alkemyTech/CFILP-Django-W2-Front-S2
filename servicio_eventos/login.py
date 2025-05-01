

#======================== Formularios para crear cuenta de usuario              =============

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Una para crear y otra para autenticar si existe
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate #Crea la cookie de sesion para el usuario

#region Crear cuenta de usuario y autenticar
def signup_view(request):
    # Si el usuario envia el formulario para crear una cuenta 'POST'	
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if request.POST.get('password1') != request.POST.get('password2'):
            if form.is_valid():
                try:
                    user = form.save() # Guarda el usuario en la base de datos y lo asigna a "user"
                    login(request, user) # Crea la cookie de sesion para el usuario
                    return redirect("home")
                except: 
                    return render(request,'servicio_eventos/sign_up.html',{
                    'form': form,
                    'error': 'Ya existe una cuenta con ese nombre. Intente nuevamente.'
                    })
        else:
            return render(request,'servicio_eventos/sign_up.html',{
                'form': form,
                'error': 'Las contraseñas no cumplen los requisitos.'
                })
    # sino es un 'POST' (GET) entonces se crea el formulario vacio
    # y se renderiza la plantilla de registro usando UserCreationForm
    # (que es un formulario de Django para crear usuarios)    
    elif request.method == 'GET': # Lo fuerzo en get porque existen metodos como PUT, PATCH, DELETE
        form = UserCreationForm()
    return render(request, 'servicio_eventos/sign_up.html', {'form': form})


def logout_view(request):
    logout(request) # Cierra la sesion del usuario (importada de django.contrib.auth)
    return redirect("home") # Redirige a la vista de marcas después de cerrar sesión

def login_view(request):
    if request.method == 'GET':
        return render(request, 'servicio_eventos/login.html', {'form': AuthenticationForm()})

    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # nombre de la ruta, no url
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'servicio_eventos/login.html', {'form': AuthenticationForm()})

#endregion
