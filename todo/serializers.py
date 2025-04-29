from rest_framework import serializers
from todo.models import ToDo

# Serializers define the API representation.
class ToDorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ['content']