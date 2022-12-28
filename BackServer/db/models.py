from django.db import models

class Item(models.Model):
    inventory = models.ForeignKey('player.inventory', on_delete=models.PROTECT, null=True)
    itemID = models.CharField(max_length=45)
    itemName = models.CharField(max_length=45)
    itemType = models.CharField(max_length=45)
    sellingValue = models.IntegerField(default=0)
    buyingValue = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

class ItemInfo(models.Model):
    itemID = models.CharField(max_length=255, primary_key=True)
    itemName = models.CharField(max_length=45)
    itemType = models.CharField(max_length=45)
    sellingValue = models.IntegerField(default=0)
    buyingValue = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

class Job(models.Model):
    jobID = models.CharField(max_length=45, primary_key=True)
    jobName = models.CharField(max_length=45)
    jobEffect = models.CharField(max_length=45)

class NPC(models.Model):
    npcID = models.CharField(max_length=45, primary_key=True)
    npcName = models.CharField(max_length=45)
    npcType = models.CharField(max_length=45)
    npcImgPath = models.CharField(max_length=45)

class Dialogue(models.Model):
    npc = models.ForeignKey('db.NPC', on_delete=models.PROTECT)
    mainCategory = models.CharField(max_length=255)
    middleCategory = models.CharField(max_length=255)
    subCategory = models.CharField(max_length=255)
    questMode = models.BooleanField()
    scene = models.CharField(max_length=255)
    dialogue = models.TextField()

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
