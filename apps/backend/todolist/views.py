from django.shortcuts import render

# Create your views here.
from .models import ToDoItem
from .serializers import ToDoItemSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class ToDoItemViewSet(APIView):
    def get(self, request):
        items = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(items, many=True)
        return Response(serializer.data)
    # queryset = ToDoItem.objects.all()
    # serializer_class = ToDoItemSerializer