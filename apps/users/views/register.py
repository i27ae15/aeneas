from apps.users.serializers import RegisterSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_spectacular.utils import (
    extend_schema, OpenApiExample, inline_serializer
)

from users.models import CustomUser as User

from users.views.serializers.register import (
    EmailSerializer, UserNameSerializer
    )


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CheckIfEmailExistAPIView(APIView):

    @extend_schema(
        description="Check if an email exists in the database.",
        request=EmailSerializer,
        responses={
            200: inline_serializer(
                name='EmailExistsResponse',
                fields={
                    'exists': 'boolean'
                }
            )
        },
        examples=[
            OpenApiExample(
                'An example response',
                summary='Email Exists',
                value={'exists': True},
                response_only=True,
                media_type='application/json'
            ),
        ],
    )
    def post(self, request):
        data: dict = request.data

        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email: str = serializer.validated_data.get('email')

        # Check in the database, user model, if the email exists
        user = User.objects.filter(email=email).first()

        if user:
            return Response({'exists': True}, status=status.HTTP_200_OK)

        return Response({'exists': False}, status=status.HTTP_200_OK)


class CheckIfUserNameExistAPIView(APIView):

    @extend_schema(
        description="Check if an username exists in the database.",
        request=UserNameSerializer,
        responses={
            200: inline_serializer(
                name='UsernameExistsResponse',
                fields={
                    'exists': 'boolean'
                }
            )
        },
        examples=[
            OpenApiExample(
                'An example response',
                summary='usarname Exists',
                value={'exists': True},
                response_only=True,
                media_type='application/json'
            ),
        ],
    )
    def post(self, request):
        data: dict = request.data

        serializer = UserNameSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        username: str = serializer.validated_data.get('username')

        user = User.objects.filter(username=username)

        if user:
            return Response({'exists': True}, status=status.HTTP_200_OK)

        return Response({'exists': False}, status=status.HTTP_200_OK)
