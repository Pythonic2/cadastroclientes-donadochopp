from .models import Client
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ["url", "name", "email", "phone_number", "trabalha", "nome_empresa"]
