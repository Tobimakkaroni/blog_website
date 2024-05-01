from django.db import models
from django.contrib.auth.models import User
from django.db import models

class ClickerUsercounter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)