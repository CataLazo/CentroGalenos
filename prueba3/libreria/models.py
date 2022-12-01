from django.db import models

# Create your models here.


class paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12, verbose_name='Rut')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    direccion = models.CharField(max_length=200, verbose_name='Direccion')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    contrasena = models.CharField(max_length=10, verbose_name='Contraseña')
    fechanac = models.DateField(verbose_name='Fecha de nacimiento')

    def __str__(self):
        fila = "Rut: " + self.rut + "-" + "Nombre: " + self.nombre + "-" + "Apellido: " + self.apellido + "-" + \
            "Direccion: " + self.direccion + "-" + "Telefono: " + \
            self.telefono + "-" + "fecha de nacimiento: " + self.fechanac
        return fila

    # class tomadehora(models.Model):
    #id= models.AutoField(primary_key=True, db_column='Increase effectiveness')
    #rut= models.CharField(max_length=12, verbose_name='Rut')
    #nombre= models.CharField(max_length=300, verbose_name='Nombre')
    #nombremedico= models.CharField(max_length=300, verbose_name= 'Nombre Medico')


class consulta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id',)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    medico = models.CharField(max_length=30, verbose_name="Medico")
    razon = models.CharField(max_length=300, verbose_name="Motivo")
    valor = models.IntegerField()
    fecha = models.DateField(verbose_name="fecha consulta")

    def __str__(self):
        fila = "Nombre: " + self.nombre + "-" + "Apellido: " + self.apellido + "-" + "Telefono: " + \
            self.telefono + "-" + "Medico" + self.medico + "-" + \
             "Valor" + self.valor + "-" + "Razon" + self.razon + "-" + "Fecha" + self.fecha
        return fila

class user(models.Model):
    rut = models.CharField(verbose_name='Rut')
    nombre = models.CharField(verbose_name='Nombre completo')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(verbose_name='Direccion')
    email = models.EmailField()
    fechaDeNac = models.DateField(verbose_name='Selecciona tu fecha de nacimiento')
    password1 = models.CharField(verbose_name='Contraseña')
    password2 = models.CharField(verbose_name=' Confirma Contraseña')
    bono = models.CharField(verbose_name='Fonasa o Isapre')