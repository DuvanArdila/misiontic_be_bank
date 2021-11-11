from rest_framework import serializers
from .models import Soporte, PQR


class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    soporte_id = SoporteSerializer(read_only=True)
    class Meta:
        model = PQR
        fields = ['id', 'soporte_id', 'tipo', 'info']
