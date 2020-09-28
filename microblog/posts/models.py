from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE);
    title = models.CharField(max_length = 100)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name = 'post_likes')
    dislikes = models.ManyToManyField(User, related_name = 'post_dislikes')

    def get_total_likes(self):
        return self.likes.count()
    
    def get_total_dislikes(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse("posts:home")
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'postcomments')
    name = models.CharField(blank = True, max_length = 50)
    created_date = models.DateTimeField(auto_now = True)
    body = models.CharField(max_length = 150)

    def get_absolute_url(self):
        return reverse("posts:postdetail", kwargs={"pk": self.post.pk})
    

    