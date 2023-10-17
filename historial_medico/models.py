from django.db import models

class Trastornos(models.Model):
    # atributos
    vasculares = models.CharField(max_length=100, null = True, blank = True)
    afasia = models.CharField(max_length=15, null = True, blank = True)
    disartria = models.CharField(max_length=15, null = True, blank = True)
    disfagia = models.BooleanField()
    disfonia = models.CharField(max_length=15, null = True, blank = True)

class ExamenFisico(models.Model):
    # atributos
    grado_funcional = models.CharField(max_length=18, null = True, blank = True)
    actitud_postural = models.CharField(max_length=18, null = True, blank = True)
    reflejos = models.CharField(max_length=12, null = True, blank = True)
    actividades_motoras = models.CharField(max_length=50, null = True, blank = True)
    coordinacion = models.BooleanField()
    orientacion = models.BooleanField()

class Observaciones(models.Model):
    # atributos
    traqueostomia = models.BooleanField()
    upp = models.BooleanField()
    control_esfinter = models.BooleanField()

class EvaluacionCorporal(models.Model):
    # atributos
    esquema_corporal = models.CharField(max_length=100, null = True, blank = True)
    sensibilidad = models.CharField(max_length=12, null = True, blank = True)
    tipo_sensibilidad = models.CharField(max_length=15, null = True, blank = True)
    nivel_fuerza = models.IntegerField()
    tono_muscular = models.CharField(max_length=15, null = True, blank = True)
    trofismo_muscular = models.CharField(max_length=15, null = True, blank = True)
    rango_articular = models.IntegerField()
    retracciones_musculares = models.CharField(max_length=100, null = True, blank = True)

class DolorInfo(models.Model):
    # atributos
    nivel = models.IntegerField()
    area = models.CharField(max_length=100, null = True, blank = True)
    punto_gatillo = models.CharField(max_length=100, null = True, blank = True)
    palpacion = models.BooleanField()
    distribucion = models.CharField(max_length=12, null = True, blank = True)
    ocurrencia = models.CharField(max_length=30, null = True, blank = True)

class Antecedentes(models.Model):
    # atributos
    diabetes = models.BooleanField()
    hta = models.BooleanField()
    cardiaco = models.BooleanField()
    operaciones = models.BooleanField()
    otros = models.CharField(max_length=200, null = True, blank = True)
    alergias = models.CharField(max_length=200, null = True, blank = True)

class Evaluacion(models.Model):
    # atributos    
    enfermedad = models.CharField(max_length=60, null = True, blank = True)
    tiempo_enfermedad = models.IntegerField()
    diagnostico_medico = models.CharField(max_length=100, null = True, blank = True)
    diagnostico_terapeutico = models.CharField(max_length=100, null = True, blank = True)
    plan_tratamiento = models.CharField(max_length=500, null = True, blank = True)
    paciente = models.ForeignKey('administracion_de_citas.Paciente', on_delete=models.CASCADE) #Unico con llave Foranea   
    antecedentes = models.OneToOneField(Antecedentes, on_delete=models.CASCADE) #De 1 a 1
    dolor_info = models.OneToOneField(DolorInfo, on_delete=models.CASCADE)
    observaciones = models.OneToOneField(Observaciones, on_delete=models.CASCADE)
    trastornos = models.OneToOneField(Trastornos, on_delete=models.CASCADE)
    examen_fisico = models.OneToOneField(ExamenFisico, on_delete=models.CASCADE)
    evaluacion_corporal = models.OneToOneField(EvaluacionCorporal, on_delete=models.CASCADE)
