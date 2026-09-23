from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)
    
    username = models.CharField(default="nemo", max_length=255)
    zipcode = models.CharField(default="", max_length=8)
    prefecture = models.CharField(default="", max_length=50)
    city = models.CharField(default="", max_length=50)
    address = models.CharField(default="", max_length=100)