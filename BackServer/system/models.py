from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class System(models.Model):
    sysID = models.CharField(max_length=45, primary_key=True)
    dateID = models.CharField(max_length=45)
    weatherID = models.CharField(max_length=45)
    timerID = models.CharField(max_length=45)
    bgmID = models.CharField(max_length=45)
    mapID = models.CharField(max_length=45)
    auth = models.CharField(max_length=45)

class Timer(models.Model):
    timerID = models.CharField(max_length=45, primary_key=True)
    timerName = models.CharField(max_length=45)
    timerType = models.CharField(max_length=45)
    timerSec = models.IntegerField()

class Weather(models.Model):
    weatherID = models.CharField(max_length=45, primary_key=True)
    weatherName = models.CharField(max_length=45)
    weatherType = models.CharField(max_length=45)
    weatherEffect = models.CharField(max_length=45)

class Date(models.Model):
    dateID = models.CharField(max_length=45, primary_key=True)
    date = models.DateField()
    dateEffect = models.CharField(max_length=45)
    darkModeYn = models.CharField(max_length=45)
    holidayYn = models.CharField(max_length=45)

class Map(models.Model):
    # mapID = models.IntegerField() # 내장 id Primary key로 대체
    name = models.CharField(verbose_name='이름', null=True, max_length=32)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    required_level = models.IntegerField(verbose_name='진입 요구 레벨 (1~100)', default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]) # TODO Character의 level과 minmax를 공유하므로, 좀 더 전역적인 상수 선언 테이블이 필요할수도?
    location = models.CharField(max_length=255, null=True, blank=True) # TODO location? 용도가?
    coordinate = models.CharField(verbose_name='좌표', max_length=255) # TODO 어떻게 활용되는지?
    street = models.CharField(max_length=255) # TODO 용도가?

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '맵'
        verbose_name_plural = verbose_name

class Bgm(models.Model):
    bgmID = models.CharField(max_length=45, primary_key=True)
    bgmName = models.CharField(max_length=45)
    bgmType = models.CharField(max_length=45)
    bgmPath = models.CharField(max_length=45)

