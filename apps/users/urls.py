from django.urls import path
from users.views import UserLoginAPIView, UserCreateAPIView

app_name = 'users'

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]

