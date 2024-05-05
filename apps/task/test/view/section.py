from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task.models.section import Section
from core.testing import print_starting, print_success

from users.tests.utils import create_user
from task.test.utils import (
    create_section,
)


class SectionAPIViewTest(APITestCase):
    # setup
    def setUp(self):
        self.user, _ = create_user()
        self.user = self.user[0]

        self.dataST = {
            'user': self.user.id,
            'name': 'section_new',
            'description': 'section_de_prueba'
        }
        self.dataSF = {
            'user': '99999999666666666666',
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
        print_starting()
        section, _ = create_section(
            related_objects={'user': self.user}
        )
        section = section[0]
        pk = section.pk
        url = reverse('task:section', kwargs={'pk': pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], section.name)
        print_success()

    def test_all_section(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_success()

    def test_noexiste_section(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    # POST
    def test_POST_created_201(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section')
        response = self.client.post(url, self.dataST, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print_success()

    def test_POST_bad_request_400(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section')
        response = self.client.post(url, self.dataSF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_success()

    # PUT
    def test_PUT_ok_200(self):
        print_starting()
        section, _ = create_section(
            related_objects={'user': self.user}
        )
        section = section[0]
        pk = section.pk
        url = reverse('task:section', kwargs={'pk': pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataSU, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_success()

    def test_PUT_dont_exist_404(self):
        print_starting()
        url = reverse('task:section', kwargs={'pk': 9999})
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataSU, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    def test_PUT_bad_request_400(self):
        print_starting()
        section, _ = create_section(
            related_objects={'user': self.user}
        )
        section = section[0]
        pk = section.pk
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section', kwargs={'pk': pk})
        response = self.client.put(url, self.dataSF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_success()

    # DELETE
    def test_section_delete(self):
        print_starting()
        section, _ = create_section(
            related_objects={'user': self.user}
        )
        section = section[0]
        pk = section.pk
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section', kwargs={'pk': pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Section.objects.filter(pk=pk).exists())
        print_success()

    def test_DELETE_dont_exist_404(self):
        print_starting()
        url = reverse('task:section', kwargs={'pk': 9999})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    def test_DELETE_created_204(self):
        print_starting()
        section, _ = create_section(
            related_objects={'user': self.user}
        )
        section = section[0]
        pk = section.pk
        self.client.force_authenticate(user=self.user)
        url = reverse('task:section', kwargs={'pk': pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print_success()
