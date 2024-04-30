from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, serializers

from users.serializers import LoginSerializer

from drf_spectacular.utils import (
    extend_schema, OpenApiExample, inline_serializer
)


class UserLoginAPIView(APIView):

    @extend_schema(
        description="Login a user and return an authentication token.",
        request=LoginSerializer,
        responses={
            200: inline_serializer(
                name='LoginSuccessResponse',
                fields={
                    'token': serializers.CharField()
                }
            ),
            400: inline_serializer(
                name='LoginErrorResponse',
                fields={
                    'detail': serializers.CharField()
                }
            )
        },
        examples=[
            OpenApiExample(
                'An example response',
                summary='Successful Login',
                value={'token': '12345abcdef'},
                response_only=True,
                media_type='application/json'
            ),
        ],
    )
    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
