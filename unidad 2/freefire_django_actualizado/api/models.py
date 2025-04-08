from django.db import models

class Atributo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"
