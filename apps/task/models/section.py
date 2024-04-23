from django.db import models

from users.models import CustomUser


class Section(models.Model):

    user: CustomUser = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=None
    )

    name = models.CharField(max_length=100)
    description = models.TextField()

    def _check_object_before_save(self):
        if self.user is None:
            raise ValueError('User is required')

    def save(self, *args, **kwargs):
        self._check_object_before_save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.user.username}'
