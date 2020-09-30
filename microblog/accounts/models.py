from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from smartfields import fields

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ACCCOUNTS = os.path.join(BASE_DIR, 'accounts/static')


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'users')
    name = models.CharField(blank = True, null = True, max_length = 50)
    email = models.EmailField(blank = True, null = True)
    profile_pic = fields.ImageField(blank = True, null = True, upload_to = 'profilepics/')
    instagram_link = models.CharField(blank = True, null = True, max_length = 50)


    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.profile_pic:
            img = Image.open(self.profile_pic.path)
            img = img.resize((1000, 1000))
            img.save(self.profile_pic.path)

    def __str__(self):
        return self.user.username