from django.shortcuts import render

# Create your views here.
from .models import ToDoItem
from .serializers import TaskSerializer, DetailTaskSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskViewSet(APIView):
    def get(self, request):
        items = ToDoItem.objects.all()
        serializer = TaskSerializer(items, many=True)
        return Response(serializer.data)
    # queryset = ToDoItem.objects.all()
    # serializer_class = ToDoItemSerializer

class DetailTaskViewSet(APIView):
    def get(self, request, pk, format=None):
        items = ToDoItem.objects.get(pk=pk)
        serializer = DetailTaskSerializer(items)
        return Response(serializer.data)
    # queryset = ToDoItem.objects.all()
    # serializer_class = ToDoItemSerializer
