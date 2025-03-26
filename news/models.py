from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    # Content and metadata fields
    title = models.CharField(max_length=100, default='', blank=True)
    content = models.TextField(default='', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title 