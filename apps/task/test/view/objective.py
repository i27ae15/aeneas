from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from task.models.section import Section
from task.models.objetives import Objective


class ObjectiveAPIViewTest(APITestCase):

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
        self.objective = Objective.objects.create(
            section=self.section,
            name='objective_new',
            description='objective_de_prueba'
        )

    def test_get_single_objective(self):
        self.client.force_authenticate(user=self.user)
        pk = self.objective.pk
        url = reverse('task:objective', kwargs={'pk': pk})
        response = self.client.get(url)
        print(f'Response data:{response.data}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.objective.name)
