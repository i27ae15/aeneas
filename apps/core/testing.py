import sys

from django.utils import timezone

from faker import Faker

from django.db.models import Model


class BColors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


fake = Faker()

FIELDS = {
    'CharField': fake.word,
    'TextField': fake.text,
    'IntegerField': fake.random_int,
    'FloatField': fake.random_int,
    'BooleanField': fake.boolean,
    'DateTimeField': lambda: timezone.make_aware(fake.date_time()),
    'email': fake.email,
    'password': fake.password,
    'username': fake.user_name,
}


class ModelCreation():

    def __init__(
        self,
        model: Model,
        objects_to_create: int = 1,
        fields_to_avoid: list[str] = ['id'],
        related_objects: dict = None,
        func_to_call=None,
        faker_seed: int = 115
    ) -> None:

        """
        Class to facilitate the creation of multiple model instances with
        specified attributes and relationships.

        Attributes:
            model (Model): The Django model class for which instances are
                created.
            objects_to_create (int): Number of instances to create
                (default 1).

            fields_to_avoid (list[str]): Fields to exclude from automatic
                population (default ['id']).

            related_objects (dict): Mapping of field names to related
                object instances to be used when creating model instances.

            func_to_call (callable): Function used to create each instance;
                defaults to the model's `objects.create()` method if not
                provided.

            faker_seed (int): Seed for Faker to ensure consistent random
                data (default 115).

        Methods:
            _get_fields_and_types: Returns a dictionary of field names and
                their data types, excluding those listed in
                `fields_to_avoid`.

            _create_information: Generates a list of dictionaries, each
                representing the data for one instance with fields
                populated accordingly.

            _create_objects: Creates and returns a list of model instances
                based on the data prepared in `_create_information`.

        Example:
            >>> model_creator = ModelCreation(User, objects_to_create=5)
            >>> created_users = model_creator.objects
        """

        Faker.seed(faker_seed)

        self.model: Model = model
        self.objects_to_create: int = objects_to_create
        self.fields_to_avoid: list[str] = fields_to_avoid
        self.related_objects: dict = related_objects or dict()
        self.func_to_call = func_to_call or self.model.objects.create

        self.fields_and_types: dict = self._get_fields_and_types()
        self.information: list[dict] = self._create_information()
        self.objects = self._create_objects()

    def _get_fields_and_types(self) -> dict[str, str]:
        """
        Compiles a dictionary mapping field names to their respective
        internal data type, excluding fields listed in `fields_to_avoid`.

        Returns:
            dict[str, str]: Dictionary of field names and data types.
        """
        fields_and_types = {
            field.name: field.get_internal_type()
            for field in self.model._meta.get_fields()
            if field.name not in self.fields_to_avoid
        }

        return fields_and_types

    def _create_information(self) -> list[dict]:
        """
        Constructs a list of dictionaries, each containing data for creating a
        model instance. Data fields are populated with values generated based
        on predefined rules or related objects.

        Returns:
            list[dict]: Data for each model instance to be created.
        """

        information = []
        special_fields = ['email', 'password', 'username']

        for _ in range(self.objects_to_create):
            data = {}
            for field, field_type in self.fields_and_types.items():
                if field in special_fields:
                    data[field] = FIELDS[field]()
                else:
                    func_info = FIELDS.get(field_type, None)
                    if func_info:
                        data[field] = func_info()
                    else:
                        # this mean this should be a related field
                        # check if the field is in the related_objects
                        # if it is, use that object, if not, put None

                        if field in self.related_objects:
                            data[field] = self.related_objects[field]
                        else:
                            data[field] = None
            information.append(data)
        return information

    def _create_objects(self) -> list[Model]:
        """
        Uses the data prepared in `_create_information` to create and return a
        list of model instances using the function specified in `func_to_call`.

        Returns:
            list[Model]: List of newly created model instances.
        """

        objects = []

        for current in range(self.objects_to_create):
            objects.append(
                self.func_to_call(
                    **self.information[current]
                )
            )

        return objects


def print_success(text: str = None, show_line: bool = True):
    if not text:
        print(f'{BColors.OKGREEN}OK{BColors.ENDC}')
    else:
        print(f'{BColors.OKGREEN}{text}{BColors.ENDC}')

    if show_line:
        print('-'*70)


def print_starting(text=None):
    if not text:
        frame = sys._getframe(1)
        func_name = frame.f_code.co_name
        print(f'{BColors.OKBLUE}Testing: {func_name}{BColors.ENDC}')
    else:
        print(f'{BColors.OKBLUE}{text}{BColors.ENDC}')


def print_warning(text):
    print(f'{BColors.WARNING}{text}{BColors.ENDC}')


def print_error(text):
    print(f'{BColors.FAIL}{text}{BColors.ENDC}')

