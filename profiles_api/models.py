from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Custom user manager for user profiles'''

    def create_user(self, email, name, password=None):
        '''Create and save a new user profile'''
        if not email:
            raise ValueError('User must have an email address')

        '''Normalize email adress'''
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        '''Set password'''
        user.set_password(password)

        user.save(using=self._db) 

        return user

    def create_superuser(self, email, name, password):
        '''Create and save new superuser'''
        user = self.create_user(email, name, password)

        user.is_superuser = True # Created automatically by PermissionMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    # Overrride of default field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retreive full name of user.'''
        return self.name

    def get_short_name(self):
        '''Retrieve short name of user.'''
        return self.name

    def __str__(self):
        '''Return string representation of object'''
        return self.email
