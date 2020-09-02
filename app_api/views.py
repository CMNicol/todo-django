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


class RetrieveAPIView(APIView):

    def get(self, request):

        controller = TodoController()
        return Response({"number of todos": controller.total, "number complete": controller.complete,
                         "number incomplete": controller.incomplete, "todos": controller.todos})



class DeleteAPIView(APIView):

    def post(self, request: Request) -> Response:
        idn = self.validate_post_request(request)

        try:
            TodoController.remove(id=idn)
            return Response("todo removed successfully")
        except:
            return Response("an error occurred removing todo from the db")

    @staticmethod
    def validate_post_request(request: Request) -> int:

        idn = request.data['id']

        # todo check if request is suitable to create model

        return idn


class AddAPIView(APIView):

    def post(self, request: Request) -> Response:

        # retrieve and validate data from request
        title, description = self.validate_post_request(request)

        # add to db
        try:
            TodoController.add(title=title, description=description)
            return Response("todo added successfully")
        except:
            return Response("an error occurred adding todo to the db")



    @staticmethod
    def validate_post_request(request: Request) -> (str, str):
        title = request.data['title']
        description = request.data['description']

        # todo check if request is suitable to create model

        return title, description

    # def post(self, request: Request):
    #     serializer = TodoItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
