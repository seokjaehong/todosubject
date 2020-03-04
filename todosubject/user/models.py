from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# from todosubject.common import TodoBase


class User(AbstractUser):
    name = models.CharField('이름', max_length=10)
    email = models.EmailField('email')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

