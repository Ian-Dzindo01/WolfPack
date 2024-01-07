from django.db import models
from django.contrib.auth.models import User
import random
from PIL import Image

class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']                # order of tweets

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
