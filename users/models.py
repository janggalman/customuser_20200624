from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
