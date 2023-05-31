from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import Http404

from .serializers import TaskSerializer
from todo.models import Task


class TodoListView(APIView):
    # adding basic authentication

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # handling the get request

        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # handling the post request

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    # adding basic authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        # getting the todo by pk otherwise return the 404 status code

        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        # handling the put request here

        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # handling the delete request here
        
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
