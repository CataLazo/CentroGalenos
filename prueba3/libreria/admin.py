from django.contrib import admin
from .models import consulta, paciente,user
# Register your models here.

admin.site.register(paciente)
admin.site.register(consulta)
admin.site.register(user)
