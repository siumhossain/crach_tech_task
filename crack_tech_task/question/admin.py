from django.contrib import admin
from question.models import FavoriteQuestion, Question, ReadQuestion

# Register your models here.
admin.site.register(Question)
admin.site.register(FavoriteQuestion)
admin.site.register(ReadQuestion)