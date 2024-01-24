from django.contrib.auth.models import Group, User
from .models import Tarea
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TareaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarea
        fields = ['url', 'id', 'titulo', 'descripcion', 'estado', 'fecha_creacion', 'fecha_fin', 'categoria']