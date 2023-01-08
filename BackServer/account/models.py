from django.contrib.auth.models import AbstractUser, Group as Django_Group
from django.db import models
from django.utils.translation import gettext_lazy as _ # Django의 기본적인 i18n translate 함수

class Group(Django_Group): # 사용자 정의 그룹
    description = models.CharField(verbose_name='설명', max_length=128, null=True, blank=True)
    class Meta:
        verbose_name = "그룹"
        verbose_name_plural = verbose_name

class User(AbstractUser): # 사용자 정의 User; 닉네임, 성별, 프로필, 상메 등의 추가 정보를 관리하기 위해 기존 Django User를 AbstractUser로부터 상속받아 확장
    nickname = models.CharField(verbose_name='닉네임', max_length=16, null=True, unique=True)
    email = models.EmailField(_("email address"))
    gender = models.BooleanField(verbose_name='성별', null=True) # 남자==False, 여자==True
    picture = models.ImageField(verbose_name='프로필 사진', upload_to='www/images/profile', null=True, blank=True) # TODO 프사 업로드 기능 필요?
    status_message = models.CharField(verbose_name='상태 메시지', max_length=32, null=True, blank=True)
    first_name = None # User의 기본 필드; 사용하지 않으므로 None
    last_name = None # User의 기본 필드; 사용하지 않으므로 None

    class Meta: # Admin 페이지에 보여질 엔티티 이름
        verbose_name = "사용자"
        verbose_name_plural = verbose_name
