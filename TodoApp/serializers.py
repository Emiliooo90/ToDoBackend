from .models import Tarea
from rest_framework import serializers

#Serializador para la tarea
class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarea
        fields = ['url', 'id', 'titulo', 'descripcion', 'estado', 'fecha_creacion', 'fecha_fin', 'categoria']