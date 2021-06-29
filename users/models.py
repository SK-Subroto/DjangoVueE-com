from django.db import models
from django.contrib.auth.models import AbstractUser
import jsonfield


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Token(models.Model):
    code = models.TextField(null=True, max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # def __str__(self):
    #     return self.id

