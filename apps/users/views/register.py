from apps.users.serializers import RegisterSerializer

from rest_framework.generics import CreateAPIView
from users.models import CustomUser as User


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
