
from django import forms

from .models import consulta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = consulta
        fields = ['nombre', 'apellido', 'telefono', 'medico', 'razon', 'fecha']


class UserRegisterForm(UserCreationForm):
    rut = forms.CharField(label='Rut')
    username = forms.CharField(label='Nombre completo')
    direccion = forms.CharField(label='direccion')
    email = forms.EmailField()
    fechaDeNac = forms.DateField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label=' Confirma Contraseña', widget=forms.PasswordInput)
    bono = forms.CharField(label='Tipo de bono medico')
    class Meta:
        model = User
        fields = ['rut','username','direccion', 'email','fechaDeNac','password1' ,'password2','bono']



