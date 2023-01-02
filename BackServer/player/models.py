from django.db import models
from account.models import Account

class PlayerCharacter(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.PROTECT)
    statusID = models.CharField(max_length=45, default=1)
    jobID = models.CharField(max_length=45, default=1)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    location = models.CharField(max_length=255, default='default_location')
    title = models.CharField(max_length=45, default=1)

class Status(models.Model):
    PlayerCharacterID = models.ForeignKey('player.PlayerCharacter', on_delete=models.PROTECT)
    Hp = models.IntegerField(default=0)
    Mp = models.IntegerField(default=0)
    Str = models.IntegerField(default=0)
    Dex = models.IntegerField(default=0)
    Con = models.IntegerField(default=0)
    Attk = models.IntegerField(default=0)
    Def = models.IntegerField(default=0)
    Hit = models.IntegerField(default=0)
    Dodge = models.IntegerField(default=0)
    Block = models.IntegerField(default=0)
    Critical = models.IntegerField(default=0)
    Agility = models.IntegerField(default=0)
    Speed = models.IntegerField(default=0)
    Friendly = models.IntegerField(default=0)
    buffID = models.IntegerField(default=0)
    debuffID = models.IntegerField(default=0)


class Inventory(models.Model):
    PlayerCharacterID = models.ForeignKey('player.PlayerCharacter', on_delete=models.PROTECT)
    money = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    weight = models.IntegerField(null=True)

# class ItemStored(models.Model):
#     ItemStoredID = models.AutoField(primary_key=True)
#     item = models.ForeignKey('db.Fish', on_delete=models.PROTECT)
#     count = 0
