from rest_framework import generics, authentication, permissions, views, status
from .models import PQR, Soporte, Bank, User
from .serializers import BankSerializer, SoporteSerializer, PQRSerializer
from rest_framework.response import Response

# Create your views here.
class SoporteListCreate(generics.ListCreateAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer


class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer


class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer


class BankListCreate(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CountUser(views.APIView):
    def get(self, request):
        queryset = User.objects.all()
        count_users = len(queryset)
        data = {"Number of users": count_users}
        return Response(data=data, status=status.HTTP_200_OK)


