from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from mongoengine import *
from importlib import import_module

# Django backend database -------------

#Base class
class Base(models.Model):
    # Base Model
    # which includes all common fields of every module
    # all modules will inherit this class
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# Country masters
class Country(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)



# User Signup in Sql ways
class UserSignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.first_name


# ActivateUser models or fields
class ActivateUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=False)
    unique_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.first_name

# Contact us models
class Contactus(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name