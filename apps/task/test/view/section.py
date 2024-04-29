from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from task.models.section import Section


class SectionAPIViewTest(APITestCase):

    def test_get_single_section(self):

        user = CustomUser.objects.create_user(
            email='newuser@gmail.com',
            username='newuser',
            password='newpassword'
            )
        section = Section.objects.create(
            name='section_new',
            user=user
        )
        pk = section.pk
        url = reverse('task:section', kwargs={'pk': pk})
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], section.name)

    def test_all_section(self):

        user = CustomUser.objects.create_user(
            email='newuser@gmail.com',
            username='newuser',
            password='newpassword'
            )
        self.client.force_authenticate(user=user)
        url = reverse('task:section')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_noexiste_section(self):
        user = CustomUser.objects.create_user(
            email='newuser@gmail.com',
            username='newuser',
            password='newpassword'
            )
        self.client.force_authenticate(user=user)
        url = reverse('task:section', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
