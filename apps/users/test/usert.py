from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from task.models.section import Section


class AuthTestCase(APITestCase):

    def test_signup(self):

        url = reverse('register/')  # Adjust URL name as per your urlpattern
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username='newuser')
        token = Token.objects.get(user=user)
        self.assertIsNotNone(token)

    def test_signup_with_section(self):

        url = reverse('register/')  # Adjust URL name as per your urlpattern
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username='newuser')
        token = Token.objects.get(user=user)
        sections = Section.objects.filter(user=user).count()
        self.assertIsNotNone(token)
        self.assertEqual(sections, 5)

    def test_login(self):

        User.objects.create_user(
            'testuser', 'testuser@example.com', 'testpassword123'
            )
        url = reverse('login/')  # Adjust URL name as per your urlpattern
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue('token' in response.data)
