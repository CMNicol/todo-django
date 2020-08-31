from .models import TodoItem
from rest_framework import serializers


class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'description')
