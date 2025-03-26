from rest_framework import serializers
from .models import Clientes

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'