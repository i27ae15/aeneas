from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task.models.objetives import Objective
from core.testing import print_starting, print_success

from users.tests.utils import create_user
from task.test.utils import (
    create_section, create_objective
)


class ObjectiveAPIViewTest(APITestCase):

    def setUp(self):
        self.user, _ = create_user()
        self.user = self.user[0]

        self.section, _ = create_section(
            related_objects={'user': self.user}
        )
        self.section = self.section[0]

        self.dataOt = {
            'section': self.section.id,
            'name': 'objective_new',
            'description': 'objective_de_prueba'
        }

        self.dataOF = {
            'section': '999911111',
            'name': 'objective_new',
            'description': 'objective_de_prueba'
        }

        self.dataOU = {
            'section': self.section.id,
            'name': 'war',
            'description': 'objective_de_prueba'
        }

    # GET
    def test_get_single_objective(self):
        print_starting()
        objective, _ = create_objective(
            related_objects={
                'section': self.section
            },
        )
        objective = objective[0]
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = objective.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': objective_pk}
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], objective.name)
        print_success()

    def test_all_objective(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        url = reverse('task:objective', kwargs={'section_pk': section_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_success()

    def test_noexiste_objective(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': 9999}
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    # POST
    def test_POST__Obejective_created_201(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        url = reverse('task:objective', kwargs={'section_pk': section_pk})
        response = self.client.post(url, self.dataOt, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print_success()

    def test_POST_Objective__bad_request_400(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        url = reverse('task:objective', kwargs={'section_pk': section_pk})
        response = self.client.post(url, self.dataOF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_success()

    # PUT
    def test_PUT_ok_200(self):
        print_starting()
        objective, _ = create_objective(
            related_objects={
                'section': self.section
            },
        )
        objective = objective[0]
        section_pk = self.section.pk
        objective_pk = objective.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': objective_pk}
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataOU, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_success()

    def test_PUT_dont_exist_404(self):
        print_starting()
        section_pk = self.section.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': 9999}
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataOU, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    def test_PUT_objective_bad_request_400(self):
        print_starting()
        objective, _ = create_objective(
            related_objects={'section': self.section}
        )
        objective = objective[0]
        section_pk = self.section.pk
        objective_pk = objective.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': objective_pk}
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataOF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_success()

    # DELETE
    def test_objective_delete(self):
        print_starting()
        objective, _ = create_objective(
            related_objects={'section': self.section}
        )
        objective = objective[0]
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = objective.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': objective_pk}
            )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Objective.objects.filter(pk=objective_pk).exists())
        print_success()

    def test_DELETE_dont_exist_404(self):
        print_starting()
        section_pk = self.section.pk
        url = reverse(
            'task:objective',
            kwargs={'section_pk': section_pk, 'objective_pk': 9999}
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()
