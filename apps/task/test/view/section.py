from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from task.models.section import Section


class SectionAPIViewTest(APITestCase):
    # setup
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='newuser@gmail.com',
            username='newuser',
            password='newpassword'
            )
        self.section = Section.objects.create(
            user=self.user,
            name='section_new',
            description='section_de_prueba'
        )
        self.dataST = {
            'user': self.user.id,
            'name': 'section_new',
            'description': 'section_de_prueba'
        }
        self.dataSF = {
            'user': '9999999999999',
            'name': 'section_new',
            'description': 'section_de_prueba'
        }
        self.dataSU = {
            'user': self.user.id,
            'name': 'section_update_name',
            'description': 'section_de_prueba'
        }

    # GET
    def test_get_single_section(self):

        pk = self.section.pk
        url = reverse('task:section', kwargs={'pk': pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.section.name)

    def test_all_section(self):

        self.client.force_authenticate(user=self.user)
        url = reverse('task:section')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_noexiste_section(self):

        self.client.force_authenticate(user=self.user)
        url = reverse('task:section', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # POST
    def test_POST_created_201(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section')
        response = self.client.post(url, self.dataST, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_POST_bad_request_400(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section')
        response = self.client.post(url, self.dataSF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # PUT
    def test_PUT_ok_200(self):
        pk = self.section.pk
        url = reverse('task:section', kwargs={'pk': pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataSU, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PUT_dont_exist_404(self):
        url = reverse('task:section', kwargs={'pk': 9999})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataSU, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_PUT_bad_request_400(self):
        pk = self.section.pk
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section', kwargs={'pk': pk})
        response = self.client.put(url, self.dataSF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # DELETE
