'''Models for band management'''
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Band(models.Model):
    '''Band model to hold data that all joined members can interact with'''
    name = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    '''Wrapper around User model that is part of a band and can relate to band things'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    picture_url = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name
