from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    email = models.EmailField()
