from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.models import User
from .models import metas

# Create your views here.

def inicio (request):
    return render(request,'usuario/inicio.html')

def InicioSesion (request):
    return render(request,'usuario/InicioSesion.html')    

def registro (request):
    return render(request,'usuario/Registro.html')    
    
def metaspagina (request):
    return render(request,'usuario/Metas.html')    

def perfil (request):
    return render(request,'usuario/perfil.html')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('inicio.html')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuario/InicioSesion.html")
    

def logout(request):
    do_logout(request)
    return redirect('InicioSesion.html')
    
def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('inicio.html')

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuario/inicio.html", {'form': form})


def registrar(request):
    n=request.POST['username']
    n1=request.POST['password']
    n2=request.POST['email']
    x= User.objects.create(username=n,password=n1)
    x.save()
    return render(request,"usuario/inicio.html")

def meta(request):
    n=request.POST['fecha']
    n1=request.POST['meta']
    n2=request.POST['desc']
    n3=request.POST['recompensa']
    y= metas.objects.create(fechameta=n,nombremeta=n1,descripcion=n2,recompensa=n3)
    y.save()
    return render(request,"usuario/perfil.html")