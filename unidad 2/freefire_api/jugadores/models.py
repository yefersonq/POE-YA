from django.db import models

class Jugador(models.Model):
    vida = models.IntegerField()
    balas = models.IntegerField()
    escudo = models.IntegerField()
    rango = models.CharField(max_length=50)

    def __str__(self):
        return f'Jugador - Rango: {self.rango}'
