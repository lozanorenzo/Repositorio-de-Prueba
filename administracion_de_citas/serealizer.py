from rest_framework import serializers
from .models import Terapista
from .models import Paciente

class TerapistaSerealizer(serializers.ModelSerializer):
    class Meta:
        #Clase
        model = Terapista
        #Campos
        fields = '__all__'
        
class PacienteSerealizer(serializers.ModelSerializer):
    class Meta:
        #Clase
        model = Paciente
        #Campos
        fields = '__all__'