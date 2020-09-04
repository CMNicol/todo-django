from .models import TodoItem
from rest_framework import serializers

"""
From Django REST framework API Guide

https://www.django-rest-framework.org/api-guide/serializers/#serializers
"Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that 
can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data." 
"""


class TodoItemSerializer(serializers.ModelSerializer):

    """
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    The ModelSerializer class is the same as a regular Serializer class, except that:
        - It will automatically generate a set of fields for you, based on the model.
        - It will automatically generate validators for the serializer, such as unique_together validators.
        - It includes simple default implementations of .create() and .update().
    """

    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'description', 'status']



# from app_api.serializers import TodoItemSerializer
# serializer = TodoItemSerializer()
# print(repr(serializer))
