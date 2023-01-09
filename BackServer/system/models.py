from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator



class Garnish(models.Model):
    name = models.CharField(verbose_name='이름', max_length=16, primary_key=True)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    image_path = models.CharField(verbose_name='이미지 경로', max_length=200, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '맵 장식물'
        verbose_name_plural = verbose_name

class GarnishArrangement(models.Model):
    garnish = models.ForeignKey(Garnish, verbose_name='장식물', related_name='garnish', on_delete=models.CASCADE, null=True)
    map = models.ForeignKey('Map', verbose_name='맵', related_name='map', on_delete=models.CASCADE, null=True, blank=True)
    x = models.IntegerField(verbose_name='X 좌표 위치', default=0)
    y = models.IntegerField(verbose_name='Y 좌표 위치', default=0)
    z = models.IntegerField(verbose_name='Z 순서', default=0)

    def __str__(self) -> str:
        return ''

class Maptype(models.Model):
    name = models.CharField(verbose_name='분류 명', max_length=16, primary_key=False)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '맵 종류'
        verbose_name_plural = verbose_name

class Map(models.Model):
    # mapID = models.IntegerField() # 내장 id Primary key로 대체
    name = models.CharField(verbose_name='이름', max_length=32, unique=True)
    type = models.ForeignKey(Maptype, verbose_name='종류', on_delete=models.SET_NULL, null=True)
    description = models.CharField(verbose_name='설명', max_length=64, blank=True)
    required_level = models.IntegerField(verbose_name='진입 요구 레벨 (1~100)', default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]) # TODO Character의 level과 minmax를 공유하므로, 좀 더 전역적인 상수 선언 테이블이 필요할수도?
    image_path = models.CharField(verbose_name='이미지 경로', max_length=200, null=True, blank=True)
    width = models.IntegerField(verbose_name='너비', default=100, validators=[MinValueValidator(100), MaxValueValidator(1000)])
    height = models.IntegerField(verbose_name='높이', default=100, validators=[MinValueValidator(100), MaxValueValidator(1000)])
    location = models.CharField(max_length=255, null=True, blank=True) # TODO location? 용도가?
    coordinate = models.CharField(verbose_name='좌표', max_length=255, null=True, blank=True) # TODO 어떻게 활용되는지?
    darkmodeYn = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True) # TODO 용도가?
    garnishes = models.ManyToManyField(Garnish, through=GarnishArrangement, verbose_name='장식물 배치', blank=True)#, on_delete=models.PROTECT, primary_key=False)
    east_map = models.OneToOneField('Map', verbose_name='동쪽으로 향하는 맵', related_name='east_map_of', null=True, blank=True, on_delete=models.PROTECT)
    west_map = models.OneToOneField('Map', verbose_name='서쪽으로 향하는 맵', related_name='west_map_of', null=True, blank=True, on_delete=models.PROTECT)
    south_map = models.OneToOneField('Map', verbose_name='남쪽으로 향하는 맵', related_name='south_map_of', null=True, blank=True, on_delete=models.PROTECT)
    north_map = models.OneToOneField('Map', verbose_name='북쪽으로 향하는 맵', related_name='north_map_of', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = '맵'
        verbose_name_plural = verbose_name

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

class Bgm(models.Model):
    bgmID = models.CharField(max_length=45, primary_key=True)
    bgmName = models.CharField(max_length=45)
    bgmType = models.CharField(max_length=45)
    bgmPath = models.CharField(max_length=45)

