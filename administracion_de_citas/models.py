from django.db import models

# Create your models here.
class Terapista(models.Model):
    dni = models.CharField(primary_key=True, unique=True,max_length=8)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    genero = models.CharField(max_length=1)
    salario = models.FloatField()
    activo = models.BooleanField()

    def __str__(self):
        return self.apellido+", "+self.nombre

class Paciente(models.Model):
    dni = models.CharField(primary_key=True, unique=True, max_length=8)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    genero = models.CharField(max_length=1)
    ocupacion = models.CharField(max_length=50)

    def __str__(self):
        return self.apellido+", "+self.nombre

class Cita(models.Model):
    asistido = models.BooleanField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    precio = models.FloatField()
    reporte = models.CharField(max_length=500)
    terapista = models.ForeignKey(Terapista, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey('historial_medico.Evaluacion', on_delete=models.CASCADE)
    
