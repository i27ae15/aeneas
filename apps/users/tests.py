from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from users.models import CustomUser
from task.models import Section


class AuthTestCase(APITestCase):

    def test_signup(self):

        url = reverse('users:register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_with_section(self):

        url = reverse('users:register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        usern = CustomUser.objects.get(username='newuser')
        sections = Section.objects.filter(user=usern)
        self.assertEqual(sections.count(), 5)

    def test_login(self):

        user_name = "testuser"
        password = 'testpassword123'
        email = 'testuser@example.com'

        CustomUser.objects.create_user(
            username=user_name, email=email, password=password
            )

        url = reverse('users:login')
        data = {
            'login_field': 'testuser@example.com',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')

        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('token' in response.data)
