from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class UserNameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
