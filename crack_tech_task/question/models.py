from django.db import models
from common.models import TimeStampAndVisibility
from user.models import User

# Create your models here.
class Question(TimeStampAndVisibility):
    question = models.CharField(max_length=250)
    option = models.JSONField()
    answer = models.IntegerField()
    explain = models.TextField()

    def __str__(self):
        return self.question

class FavoriteQuestion(TimeStampAndVisibility):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


class ReadQuestion(TimeStampAndVisibility):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
