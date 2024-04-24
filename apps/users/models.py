import datetime

from django.db import models
from django.utils import timezone
from task.models import Section

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        username: str,
        password: str,
        **extra_fields
    ) -> 'CustomUser':
        email = self.normalize_email(email)

        user: CustomUser = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        for i in range(1, 6):
            Section.objects.create(
                user=user,
                name=f'Sección {i}',
                description=f'Descripción de la Sección {i}',
            )

        return user

    def create_superuser(
        self,
        username: str,
        email: str,
        password: str,
        **extra_fields
    ) -> 'CustomUser':
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)

    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=''
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=''
    )

    phone: str = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=''
    )

    is_active: bool = models.BooleanField(default=True)
    is_staff: bool = models.BooleanField(default=False)
    is_tester: bool = models.BooleanField(default=False)
    is_admin: bool = models.BooleanField(default=False)

    objects: UserManager = UserManager()

    registration_date: datetime.datetime = models.DateTimeField(
        default=timezone.now
    )

    username: str = models.CharField(max_length=255, unique=True)

    # USER PERMISSIONS
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    # properties
    # -------------------------------------------------------------------

    # functions
    # -------------------------------------------------------------------

    @property
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def get_short_name(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
