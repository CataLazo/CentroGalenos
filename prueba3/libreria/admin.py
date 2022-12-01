from django.contrib import admin
from .models import consulta, paciente
from .forms import ConsultaForm
# Register your models here.

admin.site.register(paciente)
admin.site.register(consulta)