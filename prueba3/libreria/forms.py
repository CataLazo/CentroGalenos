
from django import forms

from .models import consulta, user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = consulta
        fields = ['nombre', 'apellido', 'telefono', 'medico', 'razon', 'fecha']


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['nombre', 'email',' password' ,'password']



