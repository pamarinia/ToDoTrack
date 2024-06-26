from rest_framework import serializers

from .models import ToDoItem

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id', 'title']

class DetailTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'date', 
                  'completed']