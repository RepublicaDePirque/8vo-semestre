from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    año = models.IntegerField()
