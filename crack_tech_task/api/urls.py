from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from api.user_info.view import UserInfoViewSet
from api.question_info.view import QuestionInfoViewSet



router = routers.DefaultRouter()

#  url
router.register('user-info', UserInfoViewSet, basename="user_info"),
router.register('question-info', QuestionInfoViewSet, basename="question_info"),


urlpatterns = [
    
]
    
urlpatterns += router.urls