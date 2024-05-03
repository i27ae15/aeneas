from django.db import models

from django.utils import timezone

from .objetives import Objective

# Create your models here.


class Task(models.Model):
    objective: Objective = models.ForeignKey(
        Objective,
        on_delete=models.CASCADE
    )

    completed_on: models.DateTimeField = models.DateTimeField(null=True)
    complete_date_obj: models.DateTimeField = models.DateTimeField(null=True)

    description: str = models.TextField()

    name: str = models.CharField(max_length=100)

    value: int = models.IntegerField(default=0)

    is_public: bool = models.BooleanField(default=False)

    relies_on = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True
    )

    created_by = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='created_tasks',
        null=True,  # this due to the objects already exist on the db
        default=None
    )

    @property
    def is_completed(self) -> bool:
        return self.completed_on is not None

    @property
    def relies_on_iter(self) -> list['Task']:
        return self.relies_on.all()

    def mark_completed(self) -> bool:

        # in order to know if the task can be completed, we need to
        # check if all the tasks that this task relies on are completed

        if self.relies_on.filter(completed_on=None).exists():
            return False

        self.completed_on = timezone.now()
        self.save()
        return True

    def _validate_before_saving(self):
        if self.created_by is None:
            raise ValueError('The task must have a creator')

    def save(self, *args, **kwargs):
        self._validate_before_saving()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.objective}'
