from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=60, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
