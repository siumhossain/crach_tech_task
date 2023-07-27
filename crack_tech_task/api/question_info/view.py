from rest_framework import viewsets
from rest_framework.response import Response 
from api.user_info.serializers import UserInfoSerializer
from user.models import User
from rest_framework.pagination import PageNumberPagination
from question.models import FavoriteQuestion
from django.db.models import Subquery, OuterRef, Case, When, Value, BooleanField, Exists
from question.models import ReadQuestion
from api.question_info.serializers import QuestionInfoSerializer
from question.models import Question


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    default_page_size = 100

    def get_page_size(self, request):
        if self.page_size_query_param in request.query_params:
            try:
                limit = int(request.query_params[self.page_size_query_param])
            except ValueError:
                limit = self.default_page_size
            return limit
        return self.default_page_size


class QuestionInfoViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionInfoSerializer
    http_method_names = ('get',)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Question.objects.only('question', 'option', 'answer', 'explain')
        favorite = self.request.query_params.get('favorite', False)
        read = self.request.query_params.get('read', False)
        unfavorite = self.request.query_params.get('unfavorite', False)
        unread = self.request.query_params.get('unread', False)

        if favorite:
            favorite_question_id = FavoriteQuestion.objects.filter(question_id=OuterRef('id')).values('question_id')
            queryset = queryset.annotate(is_favorite=Exists(favorite_question_id)).filter(is_favorite=True)
        if read:
            read_user_ids = ReadQuestion.objects.filter(question_id=OuterRef('id')).values('question_id')
            queryset = queryset.annotate(is_favorite=Exists(read_user_ids)).filter(is_favorite=True)
        if unread:
            unread_user_ids = ReadQuestion.objects.filter(question_id=OuterRef('id')).values('question_id')
            queryset = queryset.exclude(id__in=Subquery(unread_user_ids))
        if unfavorite:
            unfavorite_user_ids = FavoriteQuestion.objects.filter(question_id=OuterRef('id')).values('question_id')
            queryset = queryset.exclude(id__in=Subquery(unfavorite_user_ids))
        return queryset

