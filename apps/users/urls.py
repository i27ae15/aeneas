from django.urls import path
from users.views import UserLoginAPIView, UserCreateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]

app_name = 'users'