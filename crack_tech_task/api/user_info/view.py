from rest_framework import viewsets
from rest_framework.response import Response 
from api.user_info.serializers import UserInfoSerializer
from user.models import User
from rest_framework.pagination import PageNumberPagination
from question.models import FavoriteQuestion
from django.db.models import Subquery, OuterRef, Case, When, Value, BooleanField, Exists
from question.models import ReadQuestion


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


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    http_method_names = ('get',)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = User.objects.only('id','idname', 'display_name', 'email', 'phone')
        favorite = self.request.query_params.get('favorite', False)
        read = self.request.query_params.get('read', False)
        """
        this params just for make sure is data properly set by factory faker
        """
        if favorite:
            favorite_user_ids = FavoriteQuestion.objects.filter(user_id=OuterRef('id')).values('user_id')
            queryset = queryset.annotate(is_favorite=Exists(favorite_user_ids)).filter(is_favorite=True)

            return queryset
        if read:
            read_user_ids = ReadQuestion.objects.filter(user_id=OuterRef('id')).values('user_id')
            queryset = queryset.filter(id__in=Subquery(read_user_ids))
        return queryset