from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Tarea
from .serializers import UserSerializer, GroupSerializer, TareaSerializer

# Create your views here

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    #permission_classes = [permissions.IsAuthenticated]
