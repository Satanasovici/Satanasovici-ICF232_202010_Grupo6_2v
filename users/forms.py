from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from peluqueria.models import cliente



class CustomUserForm (UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class CustomClienteForm (UserCreationForm):
    
    class Meta:
        model = cliente
        fields = ['rut_cliente', 'edad', 'id_usuario_c']
        

        
class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [] 
        
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']