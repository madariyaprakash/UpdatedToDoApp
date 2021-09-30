from django.shortcuts import render
from api.models import Task
from api.serializers import TaskSerializer
# from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.views import APIView


#===================== class based views =====================

class ListTasks(APIView):
    """
    To get the list of tasks
    """
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)


class CreateTask(APIView):
    """
    To create task
    """
    def post(self, request, format=None):
        try:
            serializer = TaskSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse("Created Successfully!", safe=False)
        except:
            return JsonResponse("Failed to create!", safe=False)


class DetailTask(APIView):
    """
    To get the detail of the task
    """
    def post(self, request, pk, format=None):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task, many=False)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse('Record Not Found', safe=False)



class UpdateTask(APIView):
    """
    Update the task
    """
    def post(self, request, pk, format=None):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        except:
            return JsonResponse("Failed to updated!", safe=False)


class DeleteTask(APIView):
    """
    Delete the task
    """
    def post(self, request, pk, format=None):
        try:
            task = Task.objects.get(id=pk)
            task.delete()
            return JsonResponse("Deleted Successfully!", safe=False)
        except:
            return JsonResponse("Failed to delete!", safe=False)

