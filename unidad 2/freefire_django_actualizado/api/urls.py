from django.urls import path
from .views import actualizar_atributo

urlpatterns = [
    path('freefire/<str:nombre>/', actualizar_atributo),
]

from .views import formulario_atributos
urlpatterns += [path('agregar/', formulario_atributos)]
