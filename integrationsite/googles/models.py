from django.db import models
from django.contrib.auth.models import AbstractUser,User as authuser


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class UserGoogle(models.Model):
    user = models.ForeignKey(authuser, related_name='social_auth', on_delete=models.CASCADE)
    provider = models.CharField(max_length=32)
    uid = models.CharField()
    
    objects= models.Manager()

    def __str__(self):
        return str(self.user)

    class Meta:
        app_label = "google_information"
        abstract = True

    