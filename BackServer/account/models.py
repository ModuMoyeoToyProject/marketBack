from django.db import models


class Account(models.Model):
    accountID = models.CharField(max_length=255, primary_key=True)
    playerID = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)  # 사람이름
    gender = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)  # 계정아이디
    password = models.CharField(max_length=255)
