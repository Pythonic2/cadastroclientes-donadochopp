from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import Client

class ClientResource(resources.ModelResource):
    whatsapp_link = fields.Field(column_name='WhatsApp Link')

    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'phone_number', 'whatsapp_link', 'data_criada', 'trabalha', 'nome_empresa')

    def dehydrate_whatsapp_link(self, client):
        numero = str(client.phone_number)
        # Remove caracteres não numéricos
        numero = ''.join(filter(str.isdigit, numero))
        return f'https://wa.me/{numero}'

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource