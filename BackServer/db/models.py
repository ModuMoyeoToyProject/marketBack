from django.db import models

class Item(models.Model):
    itemID = models.CharField(max_length=45, primary_key=True)
    itemName = models.CharField(max_length=45)
    itemEffect = models.CharField(max_length=45)
    itemDescription = models.CharField(max_length=45)

class Job(models.Model):
    jobID = models.CharField(max_length=45, primary_key=True)
    jobName = models.CharField(max_length=45)
    jobEffect = models.CharField(max_length=45)

class NPC(models.Model):
    npcID = models.CharField(max_length=45, primary_key=True)
    npcName = models.CharField(max_length=45)
    npcType = models.CharField(max_length=45)
    npcImgPath = models.CharField(max_length=45)

class NoneActingObject(models.Model):
    objectID = models.CharField(max_length=45, primary_key=True)
    objectName = models.CharField(max_length=45)
    objectType = models.CharField(max_length=45)
    objectEffect = models.CharField(max_length=45)

class Building(models.Model):
    buildingID = models.CharField(max_length=45, primary_key=True)
    buildingName = models.CharField(max_length=45)
    mapID = models.CharField(max_length=45)
    buildingImgPath = models.CharField(max_length=45)
    darkModeYn = models.CharField(max_length=45)

class Fish(models.Model):
    fishID = models.CharField(max_length=45, primary_key=True)
    fishName = models.CharField(max_length=45)
    count = models.IntegerField(default=0)
    sellingValue = models.IntegerField()
    buyingValue = models.IntegerField()
    exp = models.IntegerField()
