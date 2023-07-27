from django.db import models

# Create your models here.
class TimeStampAndVisibility(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    # alias = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True