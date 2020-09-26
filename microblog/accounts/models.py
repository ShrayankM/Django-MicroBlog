from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'users')
    firstname = models.CharField(blank = True, null = True, max_length = 50)
    lastname = models.CharField(blank = True, null = True, max_length = 60)
    email = models.EmailField(blank = True, null = True)
    profile_pic = models.ImageField(blank = True, null = True, upload_to = 'profilepics/')
    instagram_link = models.CharField(blank = True, null = True, max_length = 50)

    def __str__(self):
        return self.user.username