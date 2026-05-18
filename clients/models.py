from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    data_criada = models.DateTimeField(auto_now_add=True)
    TRABALHA_CHOICES = [
        ("Sim", "Sim"),
        ("Não", "Não"),
    ]
    trabalha = models.CharField(max_length=3, choices=TRABALHA_CHOICES, default="Não")
    nome_empresa = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
