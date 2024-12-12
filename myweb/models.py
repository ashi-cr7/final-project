from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib import admin





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)

    def _str_(self):
        return self.user.username


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'username'

    def _str_(self):
        return self.vendor_name


class Package(models.Model):
    description = models.TextField(max_length=500)
    duration = models.IntegerField(default=0)
    destination = models.CharField(max_length=255)
    price = models.IntegerField()
    approved = models.BooleanField('Approved',default=False)
    media = models.FileField(upload_to='media/')

    def _str_(self):
        return self.destination


