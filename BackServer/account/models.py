from django.db import models


class Account(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)  # 사람이름
    gender = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)  # 계정아이디
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
