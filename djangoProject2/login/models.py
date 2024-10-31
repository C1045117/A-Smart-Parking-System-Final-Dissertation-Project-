from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)

