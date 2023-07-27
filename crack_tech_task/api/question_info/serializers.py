from rest_framework import serializers
from question.models import Question
from user.models import User

class QuestionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'option', 'answer', 'explain')