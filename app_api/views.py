from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import TodoItemSerializer
from .models import TodoItem
from django.http import JsonResponse
from pydantic import parse_obj_as
from typing import List
from django.core import serializers




class TodoAPIView(APIView):

    def post(self, request: Request) -> Response:
        todo_id = request.data['id']
        todo = TodoItem.objects.get(id=todo_id)
        # serializer = TodoItemSerializer(data=TodoItem.objects.get(id=todo_id))
        # return JsonResponse(request.data, safe=False)
        return Response({"todo": todo})

    def get(self, request):
        todos = TodoItem.objects.values()
        return Response({"todos": todos})





    # def post(self, request: Request):
    #     serializer = TodoItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
