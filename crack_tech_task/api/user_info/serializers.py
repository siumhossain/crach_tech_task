from rest_framework import serializers
from question.models import FavoriteQuestion, ReadQuestion
from user.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    favorite_question_quantity = serializers.SerializerMethodField()
    read_question_quantity = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('idname', 'display_name', 'email', 'phone', 'favorite_question_quantity', 'read_question_quantity')

    def get_favorite_question_quantity(self, obj):
        query_obj = FavoriteQuestion.objects.select_related('user_id', 'question_id').filter(user_id = obj.pk).count()

        return query_obj

    def get_read_question_quantity(self, obj):
        query_obj = ReadQuestion.objects.select_related('user_id', 'question_id').filter(user_id = obj.pk).count()

        return query_obj
