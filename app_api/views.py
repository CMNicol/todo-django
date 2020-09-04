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
from rest_framework.exceptions import ValidationError


class RetrieveAPIView(APIView):

    def get(self, request):
        controller = TodoController()
        return Response({"number of todos": controller.total, "number complete": controller.complete,
                         "number incomplete": controller.incomplete, "todos": controller.todos})


class DeleteAPIView(APIView):

    def post(self, request: Request) -> Response:

        # does the 'id' key exist in the request?
        try:
            idn = request.data['id']
        except KeyError:
            return Response('\'id\' key not found')

        # is the 'id' of type int?
        if type(idn) is int:
            TodoItem.objects.filter(id=idn).delete()
            return Response(['Todo with id = {} deleted successfully'.format(idn)])
        else:
            raise ValidationError('No \'id\' field found in request')


class AddAPIView(APIView):

    def post(self, request: Request) -> Response:

        # instantiate a serializer
        serializer = TodoItemSerializer(data=request.data)
        # validate the request, save if valid, raise ValidationError if invalid
        if serializer.is_valid():
            serializer.save()
            return Response(['Model saved successfully'])
        else:
            raise ValidationError('Data could not be serialized to fit TodoItem model')
