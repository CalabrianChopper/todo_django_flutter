from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

#GET POST PUT DELETE
class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
