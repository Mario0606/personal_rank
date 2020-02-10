from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import ClientSerializer
from ..models import Client


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (AllowAny,)
