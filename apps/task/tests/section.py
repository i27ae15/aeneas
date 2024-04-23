from django.test import TestCase

from task.models import Section

from users.models import CustomUser


class TestSection(TestCase):

    def test_create_section_with_user(self):

        user = CustomUser.objects.create_user(
            username='test',
            email='testemail@email.com',
            password='test'
        )

        section = Section.objects.create(
            user=user,
            name='Test Section',
            description='Test Description'
        )

        self.assertEqual(section.user, user)

