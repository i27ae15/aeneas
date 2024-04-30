from core.testing import ModelCreation

from task.models import Section, Objective, Task


def create_section(
    objects_to_create: int = 1,
    faker_seed: int = 115,
    related_objects: dict = None
) -> tuple[list[Section], list[dict]]:

    related_objects = related_objects or {}

    model_creator = ModelCreation(
        Section,
        objects_to_create=objects_to_create,
        faker_seed=faker_seed,
        related_objects=related_objects
    )

    return model_creator.objects, model_creator.information


def create_objective(
    objects_to_create: int = 1,
    faker_seed: int = 115,
    related_objects: dict = None
) -> tuple[list[Objective], list[dict]]:

    related_objects = related_objects or {}

    model_creator = ModelCreation(
        Objective,
        objects_to_create=objects_to_create,
        faker_seed=faker_seed,
        related_objects=related_objects
    )

    return model_creator.objects, model_creator.information


def create_task(
    objects_to_create: int = 1,
    faker_seed: int = 115,
    related_objects: dict = None,
    default_values: dict = None
) -> tuple[list[Task], list[dict]]:

    related_objects = related_objects or {}

    model_creator = ModelCreation(
        Task,
        objects_to_create=objects_to_create,
        faker_seed=faker_seed,
        related_objects=related_objects,
        default_values=default_values
    )

    return model_creator.objects, model_creator.information
