from rest_framework import serializers
from .models import Client

class UserSerializer(serializers.HyperlinkedModelSerializer):    
    whatsapp_link = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone_number', 'data_criada', 'trabalha', 'nome_empresa', 'whatsapp_link']

    def get_whatsapp_link(self, obj):
        numero = ''.join(filter(str.isdigit, obj.phone_number))
        return f'https://wa.me/{numero}'