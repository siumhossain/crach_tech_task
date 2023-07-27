
from django.core.management.base import BaseCommand
from question.factory import QuestionFactory

class Command(BaseCommand):
    help = 'Generates fake data using Faker'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake question to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for _ in range(count):
            question = QuestionFactory.create()
            self.stdout.write(self.style.SUCCESS(f'Created question: {question.question}'))