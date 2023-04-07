from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class ActionType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class Action(models.Model):
    content = models.TextField(blank=False, null=False)
    money = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    action_type = models.ForeignKey(ActionType, on_delete=models.SET_NULL, null=True)
