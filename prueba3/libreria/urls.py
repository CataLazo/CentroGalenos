from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('nosotros', views.nosotros , name='nosotros'),
    path('index', views.pacientes, name='pacientes'),
    path('crear', views.crear, name='crear'),
    path('delete', views.delete, name='delete'),
    path('iniciodesesion', views.sesion, name='iniciodesesion'),
    path('perfilpaciente', views.perfil, name='perfil'),
    
    path('registro/',views.registro , name='registro'),
    path('login', LoginView.as_view(template_name='pacientes/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='pacientes/logout.html'), name='Logout'),

    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)