from django.db import models

# Create your models here.
class Vhs(models.Model):
    def __str__(self):
        return f"{self.titulo}"
    titulo = models.CharField(max_length=60)
    genero = models.CharField(max_length=30)
    anioLanzamiento = models.IntegerField()
    director = models.CharField(max_length=60)

class Cds(models.Model):
    def __str__(self):
        return f"{self.artista} - {self.nombre}"
    nombre = models.CharField(max_length=60)
    artista = models.CharField(max_length=60)
    anioLanzamiento = models.IntegerField()
    genero = models.CharField(max_length=30)

class Videojuegos(models.Model):
    def __str__(self):
        return f"{self.nombre} - {self.plataforma}"
    nombre = models.CharField(max_length=60)
    desarrolladora = models.CharField(max_length=60)
    plataforma = models.CharField(max_length=60)
    genero = models.CharField(max_length=30)
