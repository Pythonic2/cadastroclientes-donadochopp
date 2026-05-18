from rest_framework import permissions, viewsets
from .models import Client
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """

    queryset = Client.objects.all().order_by("-data_criada")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
