from django.test import TestCase

from users.tests.utils import create_user


class UserTestCase(TestCase):
    def test_create_user(self):
        create_user()
