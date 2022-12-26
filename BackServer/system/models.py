from django.db import models

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
    mapID = models.IntegerField()
    location = models.CharField(max_length=255)
    required_level = models.IntegerField()
    coordinate = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

class Bgm(models.Model):
    bgmID = models.CharField(max_length=45, primary_key=True)
    bgmName = models.CharField(max_length=45)
    bgmType = models.CharField(max_length=45)
    bgmPath = models.CharField(max_length=45)

