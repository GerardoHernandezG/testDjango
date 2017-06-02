from django.db import models


class Articulos(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField()

class Comentario(models.Model):
    nombre = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_pub = models.DateTimeField('fecha publicacion')
    articulo = models.ForeignKey(Articulos)

class Usuarios(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
