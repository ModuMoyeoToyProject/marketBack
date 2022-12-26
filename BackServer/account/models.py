from django.db import models

class Account(models.Model):
    accountID = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

