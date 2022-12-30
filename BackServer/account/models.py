from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

class Group(Group):
    class Meta:
        verbose_name = "그룹"
        verbose_name_plural = "그룹"

class User(AbstractUser):
    nickname = models.CharField(verbose_name='닉네임', max_length=16, null=True, blank=False)
    email = models.EmailField(_("email address"), blank=False)
    gender = models.BooleanField(verbose_name='성별', null=True, blank=True)
    picture = models.ImageField(verbose_name='프로필 사진', upload_to='www/images/profile', null=True, blank=True)
    status_message = models.CharField(verbose_name='상태 메시지', max_length=32, null=True, blank=True)
    first_name = None
    last_name = None

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
    

class Account(models.Model):
    accountID = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
