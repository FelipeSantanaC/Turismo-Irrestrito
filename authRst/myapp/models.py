from django.db import models
from myapp.idChecker import IDChecker

# Create your models here.

class User(models.Model):
    id = models.BigAutoField(primary_key=True, default=IDChecker)
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=45,blank=False, default='')
    password = models.CharField(max_length=45,blank=False, default='')
