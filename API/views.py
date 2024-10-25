from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, Book, Author
from .serializers import TaskSerializer, BookSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


# Create your views here.

@api_view(['GET'])
def getapi(request):
    return Response({'message': 'Hello, World!'})

# Task er jonno get and post method
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# Task er jonno get, put and delete method
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'message': 'Task not found'}, status=404)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)
    


# Class based view
class TaskViewSets(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Class based view for Book
class BookViewSets(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Class based view for Author
class AuthorViewSets(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer