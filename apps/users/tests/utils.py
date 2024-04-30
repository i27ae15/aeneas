from core.testing import ModelCreation

from users.models import CustomUser as User


def create_user(
    users_to_create: int = 1,
    faker_seed: int = 115
) -> tuple[list[User], list[dict]]:

    fields_to_avoid = [
        'id',
        'logentry',
        'auth_token',
        'groups',
        'user_permissions',
    ]

    model = ModelCreation(
        model=User,
        objects_to_create=users_to_create,
        fields_to_avoid=fields_to_avoid,
        faker_seed=faker_seed,
        func_to_call=User.objects.create_user,
    )

    objects: list[User] = model.objects

    return objects, model.information
