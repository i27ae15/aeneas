from django.test import TestCase

from task.models import Section

from users.models import CustomUser


class TestSection(TestCase):

    def setUp(self):
        self.user_A = CustomUser.objects.create_user(
            username='test',
            email='testemail@email.com',
            password='test'
        )

        self.section_A = Section.objects.create(
            user=self.user_A,
            name='Test Section',
            description='Test Description'
        )

    def test_create_section_with_user(self):
        self.assertEqual(self.section_A.user, self.user_A)
        self.assertEqual(self.section_A.name, 'Test Section')
        self.assertEqual(self.section_A.description, 'Test Description')
