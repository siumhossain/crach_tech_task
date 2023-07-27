import factory
from factory.faker import Faker
from faker import Faker
from factory.fuzzy import FuzzyText


from .models import Question

FAKE = Faker()

class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question = factory.Sequence(lambda n: FuzzyText(length=10).fuzz())
    option = factory.LazyFunction(lambda: {
        "option1": FuzzyText(length=10).fuzz(),
        "option2": FuzzyText(length=10).fuzz(),
        "option3": FuzzyText(length=10).fuzz(),
        "option4": FuzzyText(length=10).fuzz(),
    })
    answer = factory.Sequence(lambda n: n % 4 + 1)
    explain = factory.Faker('paragraph')