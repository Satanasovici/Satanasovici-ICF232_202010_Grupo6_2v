from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout as do_logout
from .forms import UserDeleteForm
from django.contrib import messages
from .forms import CustomUserForm, EditProfileForm

def welcome(request):
    return render(request, "welcome.html")


def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(data=request.POST)
        if form.is_valid():

            user = form.save()

            if user is not None:
                do_login(request, user)
                return redirect('/prueba')

    return render(request, "register.html", {'form': form})



def loginCliente(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)

            
            if user is not None:
                
                do_login(request, user)
               
                return redirect('/index')
   
        # Si llegamos al final renderizamos el formulario
    return render(request, "loginCliente.html", {'form': form})


def index_cliente(request):
    if request.user.is_authenticated:
        return render(request, "index_cliente.html")
    return redirect('/')
    
 

def config(request):
    if request.user.is_authenticated:
        return render(request, "opcionesCuenta.html")
    return redirect('/')



#editadas

def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Tu cuenta ha sido borrada.')
        return redirect('/prueba')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, "borrarCuenta.html", context)





def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('/prueba')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, "Editar_Perfil.html", {'form': form})

    
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/prueba')
        else:
            return redirect('/password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, "cambiarClave.html", {'form': form})







#NUEVAS PAGINAS



def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)

            
            if user is not None:
                
                do_login(request, user)
               
                return redirect('/prueba')
   
        # Si llegamos al final renderizamos el formulario
    return render(request, "pagina_iniciar_sesion.html", {'form': form})



def logout(request):
    do_logout(request)
    return redirect('/prueba')
