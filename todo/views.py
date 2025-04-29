from rest_framework import viewsets
from todo.models import ToDo
from todo.serializers import ToDorSerializer

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDorSerializer