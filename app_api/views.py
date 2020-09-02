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
from .controller import TodoController


class TodoAPIView(APIView):

    def post(self, request: Request) -> Response:

        title, description = self.validate_post_request(request)

        return Response({"todo": title})

    def get(self, request):

        controller = TodoController()
        return Response({"number of todos": controller.total, "number complete": controller.complete,
                         "number incomplete": controller.incomplete, "todos": controller.todos})

    @staticmethod
    def validate_post_request(request: Request) -> (str, str):
        title = request.data['title']
        description = request.data['description']

        # check if request is suitable to create model

        return title, description


    # def post(self, request: Request):
    #     serializer = TodoItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
