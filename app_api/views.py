from django.http import Http404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import TodoItemSerializer
from rest_framework.serializers import ValidationError as SerialValError
from .models import TodoItem
from .controller import TodoController
from rest_framework.exceptions import ValidationError


class RetrieveAPIView(APIView):

    def get(self, request):
        controller = TodoController()
        return Response({"number of todos": controller.total, "number complete": controller.complete,
                         "number incomplete": controller.incomplete, "todos": controller.todos})


class DeleteAPIView(APIView):

    def post(self, request: Request) -> Response:
        """
        Format of request:
        {
            "id": 1,
        }
        """

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
        """
        Format of request:
        {
            "title": "to do title",
            "description": "blah blah",
        }
        """

        # instantiate a serializer
        serializer = TodoItemSerializer(data=request.data)
        # validate the request, save if valid, raise ValidationError if invalid
        if serializer.is_valid():
            serializer.save()
            return Response(['Model saved successfully'])
        else:
            raise ValidationError('Data could not be serialized to fit TodoItem model')


class EditAPIView(APIView):

    def post(self, request: Request):

        """
        Format of request:
        {
            "id": 1,
            "<field to edit>": "blah blah",
            "<another field to edit>": "blah blah"
        }
        """
        try:
            idn = request.data['id']
            instance = TodoItem.objects.get(id=idn)
            serializer = TodoItemSerializer(instance=instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('Todo with id = {} edited successfully'.format(idn))
        except KeyError:
            raise ValidationError('\'id\' key not found')
        except SerialValError:
            raise ValidationError('Serialization error')
        except TodoItem.DoesNotExist:
            raise ValidationError('Todo with id = {} not found'.format(idn))
