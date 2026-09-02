from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email = self.normalize_email(email),
        )
        
        user.set_passwrod(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    class User(AbstractBaseUser):
        email = models.EmailField(
            max_length = 255,
            unique = True,
        )
        
        is_active = models.BooleanField(default=True)
        is_admin = models.BooleanField(default=False)