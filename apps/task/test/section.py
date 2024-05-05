from django.test import TestCase

from task.models import Section

from core.testing import print_starting, print_success

from users.tests.utils import create_user
from task.test.utils import (
    create_section,
)


class TestSection(TestCase):

    def setUp(self) -> None:
        self.user, _ = create_user()
        self.user = self.user[0]

    def test_create_section_with_user(self):
        print_starting()
        self.section, _ = create_section(
            related_objects={'user': self.user}
        )
        self.section = self.section[0]
        userS = Section.objects.get(user=self.user, name='war')
        self.assertEqual(self.section.name, userS.name)
        print_success()
