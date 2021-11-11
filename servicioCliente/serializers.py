from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Soporte, PQR


class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR
        fields = ['id', 'soporte_id', 'tipo', 'info']
