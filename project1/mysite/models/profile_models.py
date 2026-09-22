from django.db import models

class Profile(models.Model):
    username = models.CharField(default="nemo", max_length=255)
    zipcode = models.CharField(default="", max_length=8)
    prefecture = models.CharField(default="", max_length=50)