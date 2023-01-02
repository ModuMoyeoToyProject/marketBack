from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _ # Django의 기본적인 i18n translate 함수

class Group(Group): # 사용자 정의 그룹
    class Meta:
        verbose_name = "그룹"
        verbose_name_plural = "그룹"

class User(AbstractUser): # 사용자 정의 User; 닉네임, 성별, 프로필, 상메 등의 추가 정보를 관리하기 위해 기존 Django User를 AbstractUser로부터 상속받아 확장
    nickname = models.CharField(verbose_name='닉네임', max_length=16, null=True, blank=False)
    email = models.EmailField(_("email address"), blank=False)
    gender = models.BooleanField(verbose_name='성별', null=True, blank=True) # TODO 성별 구분 기능 필요?
    picture = models.ImageField(verbose_name='프로필 사진', upload_to='www/images/profile', null=True, blank=True) # TODO 프사 업로드 기능 필요?
    status_message = models.CharField(verbose_name='상태 메시지', max_length=32, null=True, blank=True)
    first_name = None # User의 기본 필드; 사용하지 않으므로 None
    last_name = None # User의 기본 필드; 사용하지 않으므로 None

    class Meta: # Admin 페이지에 보여질 엔티티 이름
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
    

# TODO: 폐기 예정
class Account(models.Model):
    accountID = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
