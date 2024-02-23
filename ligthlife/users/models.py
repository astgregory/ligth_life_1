from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    location = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user}'
