from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    login_field = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username=data['login_field'],
            password=data['password']
        )
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
