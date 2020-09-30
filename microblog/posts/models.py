from django.db import models
from django.contrib.auth.models import User
from django.forms import widgets
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ["-created_date"]
    author = models.ForeignKey(User, on_delete = models.CASCADE);
    title = models.CharField(max_length = 100)
    # body = models.TextField()
    body = RichTextField(blank = True, null = True)
    likes = models.ManyToManyField(User, related_name = 'post_likes')
    dislikes = models.ManyToManyField(User, related_name = 'post_dislikes')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    description = models.CharField(max_length = 255, blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_total_likes(self):
        return self.likes.count()
    
    def get_total_dislikes(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse("posts:home")
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ["-created_date"]
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'postcomments')
    name = models.CharField(blank = True, max_length = 50)
    created_date = models.DateTimeField(auto_now = True)
    body = models.CharField(max_length = 150)

    def get_absolute_url(self):
        return reverse("posts:postdetail", kwargs={"pk": self.post.pk})

    

    