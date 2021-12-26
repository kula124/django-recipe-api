from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):
  
  def create_user(self, email, password=None, **args):
    """Creates and saves new user"""
    user = self.model(email=email, **args)
    user.set_password(password)
    user.save(using=self._db)

    return user

class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model supporting email vs username"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()
  USERNAME_FIELD = 'email'
