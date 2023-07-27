
from django.core.management.base import BaseCommand
from user.factory import UserFactory

class Command(BaseCommand):
    help = 'Generates fake data using Faker'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake users to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for _ in range(count):
            user = UserFactory.create()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.display_name}'))
