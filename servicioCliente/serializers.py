from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Bank, Soporte, PQR

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    soporte_id = SoporteSerializer(read_only=True)
    class Meta:
        model = PQR
        fields = ['id', 'soporte_id', 'tipo', 'info']


class BankSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = Bank
        fields = ["id", "name", "users"]
