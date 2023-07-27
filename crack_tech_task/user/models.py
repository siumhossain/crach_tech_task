from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class User(AbstractUser):
    idname = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    display_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.display_name