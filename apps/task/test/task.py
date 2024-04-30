from django.test import TestCase

from core.testing import print_starting, print_success

from users.tests.utils import create_user
from task.test.utils import (
    create_section,
    create_objective,
    create_task
)


class TaskModelTest(TestCase):

    def setUp(self) -> None:
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

        return super().setUp()

    def test_mark_completed_no_rely(self):

        print_starting()

        task, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective,
            },
            default_values={'completed_on': None}
        )
        task = task[0]

        self.assertFalse(task.is_completed)
        task.mark_completed()
        self.assertTrue(task.is_completed)

        print_success()

    def test_mark_completed_with_rely(self):

        print_starting()

        tasks, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective
            },
            default_values={'completed_on': None},
            objects_to_create=3
        )

        task, _ = create_task(
            related_objects={
                'created_by': self.user,
                'objective': self.objective,
                'relies_on': tasks
            },
            default_values={'completed_on': None}
        )
        task = task[0]

        self.assertFalse(task.is_completed)
        task.mark_completed()
        self.assertFalse(task.is_completed)

        # Go through each task and mark them as completed

        for t in task.relies_on_iter:
            # still the task should not be able to be completed
            # we put first the task to be completed
            # to avoid being true when all the relies tasks are completed
            task.mark_completed()
            self.assertFalse(task.is_completed)

            t.mark_completed()
            self.assertTrue(t.is_completed)

        # now the task should be able to be completed
        task.mark_completed()
        self.assertTrue(task.is_completed)

        print_success()
