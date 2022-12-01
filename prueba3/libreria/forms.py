
from django import forms

from .models import consulta, user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = consulta
        fields = ['nombre', 'apellido', 'telefono', 'medico', 'razon', 'fecha']


class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre completo')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label=' Confirma Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = user
        fiedls = ['nombre', 'email',' password1' ,'password2']



