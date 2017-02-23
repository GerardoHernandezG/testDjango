from django.db import models


class Articulos(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField()
