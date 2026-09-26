from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Tag(models.Model):
    slug = models.CharField(primary_key=True, unique=True, max_length=20)
    name = models.CharField(unique=True, max_length=20)

class Article(models.Model):
    title = models.CharField(default="", max_length=63)
    text = models.TextField(default="")
    author = models.CharField(default="", max_length=63)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    count = models.IntegerField(default=0)
    
class Comment(models.Model):
    comment = models.TextField(default="", max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)