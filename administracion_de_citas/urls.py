from django.urls import path, include
from rest_framework import routers
from administracion_de_citas import views
from .views import PacienteView

#ESPACIO DE ROUTERS
router1 = routers.DefaultRouter()
router1.register(r'terapista',views.TerapistaView,'terapista')

router2 = routers.DefaultRouter()
router2.register(r'paciente', PacienteView, 'paciente')

#ESPACIO DE URL
urlpatterns = [
    #path (Ruta , urlGeneradaPorRouter)
    path("",include(router1.urls)),
    path("",include(router2.urls))
]
