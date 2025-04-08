from rest_framework import viewsets
from .models import Jugador
from .serializers import JugadorSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
