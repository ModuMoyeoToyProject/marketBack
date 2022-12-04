from django.db import models

class PlayerCharacter(models.Model):
    playerID = models.CharField(max_length=45, primary_key=True)
    statusID = models.CharField(max_length=45)
    jobID = models.CharField(max_length=45)
    inventoryID = models.CharField(max_length=45)
    level = models.IntegerField()
    exp = models.IntegerField()
    title = models.CharField(max_length=45)

class Status(models.Model):
    statusID = models.CharField(max_length=45, primary_key=True)
    Hp = models.IntegerField()
    Mp = models.IntegerField()
    Str = models.IntegerField()
    Dex = models.IntegerField()
    Con = models.IntegerField()
    Attk = models.IntegerField()
    Def = models.IntegerField()
    Hit = models.IntegerField()
    Dodge = models.IntegerField()
    Block = models.IntegerField()
    Critical = models.IntegerField()
    Agility = models.IntegerField()
    Speed = models.IntegerField()
    Friendly = models.IntegerField()
    buffID = models.IntegerField()
    debuffID = models.IntegerField()

class Inventory(models.Model):
    inventoryID = models.CharField(max_length=45, primary_key=True)
    weight = models.IntegerField()
    quantity = models.IntegerField()
