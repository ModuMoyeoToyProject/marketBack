from django.db import models
from account.models import Account

class PlayerCharacter(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    playerID = models.AutoField(primary_key=True)
    statusID = models.CharField(max_length=45)
    jobID = models.CharField(max_length=45, null=True)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    title = models.CharField(max_length=45, null=True)

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
    playerCharacter = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE)
    inventoryID = models.AutoField(primary_key=True)
    weight = models.IntegerField(null=True)
    quantity = models.IntegerField(default=0)
