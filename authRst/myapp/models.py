from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=45,blank=False, default='')
    password = models.CharField(max_length=45,blank=False, default='')
