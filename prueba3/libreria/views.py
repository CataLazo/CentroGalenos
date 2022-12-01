from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ConsultaForm
from .forms import UserRegisterForm
from .models import consulta, paciente

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from django.core.urlresolvers import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
    
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def sesion(request):
    return render(request, 'pacientes/iniciodesesion.html')

def delete(request):
    consultas = consulta.objects.all()
    return render(request, 'pacientes/delete.html', {'consultas': consultas})

def perfil(request):
    return render(request, 'pacientes/perfil.html')
    
def pacientes(request):
    consultas = consulta.objects.all()
    return render(request, 'pacientes/index.html', {'consultas': consultas})

def crear(request):
    formulario = ConsultaForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request, 'pacientes/crear.html', {'formulario': formulario})

def eliminar(request, id):
    consultas = consulta.objects.get(id=id)
    consultas.delete()
    return redirect('pacientes')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('inicio')
    else:
        form = UserCreationForm()
    context = { 'form' : form }
    return render(request, 'pacientes/registro.html', context)

    

    

