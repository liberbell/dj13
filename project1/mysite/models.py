from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(default="", blank=True, null=True, max_length=63)
    text = models.TextField(default="")
    author = models.CharField(default="", max_length=63)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)