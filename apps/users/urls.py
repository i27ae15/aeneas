from django.urls import path
from users.views import (
    UserLoginAPIView, UserCreateAPIView, CheckIfEmailExistAPIView
)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path(
        'check_if_email_exists/',
        CheckIfEmailExistAPIView.as_view(),
        name='check_if_email_exists'
    )
]
