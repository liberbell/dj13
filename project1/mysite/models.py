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
        
        user.set_password(password)
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
        
        objects = UserManager()
        
        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = []
        
        def __str__(self):
            return self.email
        
        def has_perm(self, perm, obj=None):
            "Does the user have a specific permission?"
            return True
        
        def has_module_perm(self, app_lebel):
            "Does the user have permission to view the app `app_level`?"
            return True
        
        @property
        def is_staff(self):
            "Is the user a member of staff?"
            return self.is_admin