from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer

# Create your views here

#Vista que trae todos los datos que hay en el modelo tarea
class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    #permission_classes = [permissions.IsAuthenticated]
