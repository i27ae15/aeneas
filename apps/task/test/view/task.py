from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task.models.task import Task
from core.testing import print_starting, print_success

from users.tests.utils import create_user
from task.test.utils import (
    create_section, create_objective,
    create_task
)


class TaskAPIViewTest(APITestCase):
    def setUp(self):
        self.user, _ = create_user()
        self.user = self.user[0]

        self.section, _ = create_section(
            related_objects={'user': self.user}
        )
        self.section = self.section[0]

        self.objective, _ = create_objective(
            related_objects={'section': self.section}
        )
        self.objective = self.objective[0]

        self.dataTt = {
            'objective': self.objective.id,
            'created_by': self.user.id,
            'name': 'objective_new',
            'description': 'objective_de_prueba'
        }

        self.dataTF = {
            'objective': '3333333022222222',
            'created_by': '320000132',
            'name': 'objective_new',
            'description': 'objective_de_prueba'
        }

        self.dataTU = {
            'objective': self.objective.id,
            'created_by': self.user.id,
            'name': 'objective_new',
            'description': 'objective_de_prueba'
        }

    # GET
    def test_get_single_task(self):
        print_starting()

        task, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective,
            },
            default_values={'completed_on': None}
        )
        task = task[0]

        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        task_pk = task.pk

        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': task_pk
                }
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], task.name)
        print_success()

    def test_all_task(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        url = reverse('task:task', kwargs={
            'section_pk': section_pk,
            'objective_pk': objective_pk
            }
                      )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_success()

    def test_noexiste_task(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': 9999
                }
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    # POST
    def test_POST__task_created_201(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        url = reverse('task:task',
                      kwargs={
                          'section_pk': section_pk,
                          'objective_pk': objective_pk
                          }
                      )
        response = self.client.post(url, self.dataTt, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print_success()

    def test_POST_task__bad_request_400(self):
        print_starting()
        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        url = reverse('task:task',
                      kwargs={
                          'section_pk': section_pk,
                          'objective_pk': objective_pk
                          }
                      )
        response = self.client.post(url, self.dataTF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_success()

    # PUT
    def test_PUT_ok_200(self):
        print_starting()
        task, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective,
            },
            default_values={'completed_on': None}
        )
        task = task[0]

        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        task_pk = task.pk
        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': task_pk
                }
            )
        response = self.client.put(url, self.dataTU, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print_success()

    def test_PUT_dont_exist_404(self):
        print_starting()
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': 999999
                }
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataTU, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()

    def test_PUT_objective_bad_request_400(self):
        print_starting()
        task, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective,
            },
            default_values={'completed_on': None}
        )
        task = task[0]

        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        task_pk = task.pk
        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': task_pk
                }
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, self.dataTF, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print_success()

    # DELETE
    def test_task_delete(self):
        print_starting()
        task, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective,
            },
            default_values={'completed_on': None}
        )
        task = task[0]

        self.client.force_authenticate(user=self.user)
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        task_pk = task.pk
        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': task_pk
                }
            )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=objective_pk).exists())
        print_success()

    def test_DELETE_dont_exist_404(self):
        print_starting()
        section_pk = self.section.pk
        objective_pk = self.objective.pk
        url = reverse(
            'task:task',
            kwargs={
                'section_pk': section_pk,
                'objective_pk': objective_pk,
                'task_pk': 999999
                }
            )
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print_success()
