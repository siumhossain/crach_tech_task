import random
from django.core.management.base import BaseCommand
from question.models import Question, FavoriteQuestion
from user.models import User

class Command(BaseCommand):
    help = 'Create FavoriteQuestion objects with random user and question IDs'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of FavoriteQuestion objects to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        users = User.objects.all()
        questions = Question.objects.all()

        favorite_questions_created = 0

        for _ in range(count):
            print(f"creating {favorite_questions_created} object")
            user = random.choice(users)
            question = random.choice(questions)

            favorite_question, created = FavoriteQuestion.objects.get_or_create(
                user_id=user,
                question_id=question
            )

            if created:
                favorite_questions_created += 1

        self.stdout.write(self.style.SUCCESS(f"Created {favorite_questions_created} FavoriteQuestion objects"))