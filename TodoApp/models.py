from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=255, default="No completada")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    categoria = models.CharField(max_length=100, default="No importante")
