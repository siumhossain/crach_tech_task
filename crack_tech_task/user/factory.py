import factory
from factory.faker import Faker
from faker import Faker
from django.contrib.auth.hashers import make_password

from .models import User

FAKE = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    display_name = factory.LazyFunction(lambda: FAKE.name())
    username = factory.Sequence(lambda n: f"user{n}")
    phone = FAKE.phone_number()
    email = FAKE.email()
    # password = factory.LazyFunction(lambda: make_password(FAKE.password(length=10)))
    """
    take to time make hash password that's why i turn it off
    """
    password = factory.LazyFunction(lambda: FAKE.password(length=10))